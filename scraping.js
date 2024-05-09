const axios = require('axios');
const fs = require('fs').promises;
const cheerio = require('cheerio');

async function numbersToFiles(week, problems) {
    await Promise.all(problems.map(async item => {
        let limit_item = [];
        let limit_content = [];
        let title;
        let description;
        let input;
        let output;
        let sampleCount = 0;
        let sampleInputs = [];
        let sampleOutputs = [];

        try {
            const headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            };

            const { data } = await axios.get(`https://www.acmicpc.net/problem/${item}`, {
                headers: headers
            });

            let $ = cheerio.load(data);
            title = $('#problem_title').text();

            $("#problem-info").find('th').each((idx, item) => {
                limit_item.push($(item).text().trim());
            });

            $("#problem-info").find('td').each((idx, item) => {
                limit_content.push($(item).text().trim());
            });

            description = $("#problem_description").find('p').text().trim();
            input = $("#problem_input").find('p').text().trim();
            output = $("#problem_output").find('p').text().trim();

            while (1) {
                if ($(`#sampleinput${sampleCount+1}`).find("h2").text() !== "") {
                    let input = $(`#sampleinput${sampleCount+1}`).find("pre").text();
                    let output = $(`#sampleoutput${sampleCount+1}`).find("pre").text();
                    sampleInputs.push(input);
                    sampleOutputs.push(output);
                    sampleCount++;
                } else {
                    break;
                }
            }

            let result = `# boj_${item} ${title}

<a href="https://www.acmicpc.net/problem/${item}">문제 바로 가기</a>
            
| **${limit_item[0]}** | **${limit_item[1]}** | **${limit_item[2]}** | **${limit_item[3]}** | **${limit_item[4]}** | **${limit_item[5]}** |
| ------------- | --------------- | -------- | -------- | ------------- | ------------- |
| **${limit_content[0]}** | **${limit_content[1]}** | **${limit_content[2]}** | **${limit_content[3]}** | **${limit_content[4]}** | **${limit_content[5]}** |

### 문제

${description}

### 입력
            
${input}
            
### 출력

${output}

`;
            let inputAndOutput="";
            for(let i=0;i<sampleCount;i++){
                inputAndOutput=inputAndOutput+`### 예제 입력${i+1}\n\n\`\`\`\n${sampleInputs[i]}\`\`\`\n\n### 예제 출력${i+1}\n\n\`\`\`\n${sampleOutputs[i]}\`\`\`\n\n`;
            }
            result=result+inputAndOutput;
            try {
            await fs.mkdir(`week${week}/boj_${item}(${title})/${item}_sy`, { recursive: true });
            await fs.mkdir(`week${week}/boj_${item}(${title})/${item}_doin`, { recursive: true });
            await fs.mkdir(`week${week}/boj_${item}(${title})/${item}_sun`, { recursive: true });
            await fs.mkdir(`week${week}/boj_${item}(${title})/${item}_uk`, { recursive: true });
            await fs.writeFile(`week${week}/boj_${item}(${title})/problem.md`, result);
            console.log(`File for problem ${item} created successfully.`);
            } catch (e) {
                console.error(`Error creating file for problem ${item}:`, e);
            }
        } catch (e) {
            console.error(`Error processing problem ${item}:`, e);
        }
    }));
}

numbersToFiles(6, [11559,1111,12100,3190,5397]);
