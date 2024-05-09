// #include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
using namespace std;
char arr[12][6];
int checked[12][6] = {0}; // 0: 확인안됨 1: 터짐 2: 안터짐 3: 연계까지는 확인
void resetChecked()
{
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            checked[i][j] = 0;
        }
    }
    return;
}
bool checkNbd(int i, int j)
{
    int n = 1;
    char ch = arr[i][j];
    // cout<<ch<<"\n";
    queue<pair<int, int>> willVisit;
    willVisit.push({i, j});
    checked[i][j] = 3;
    while (willVisit.size() != 0)
    {
        int x = willVisit.front().first;
        int y = willVisit.front().second;
        willVisit.pop();
        if (x != 0 && checked[x - 1][y] == 0 && ch == arr[x - 1][y])
        {
            checked[x - 1][y] = 3;
            willVisit.push({x - 1, y});
            n++;
        }
        if (y != 0 && checked[x][y - 1] == 0 && ch == arr[x][y - 1])
        {
            checked[x][y - 1] = 3;
            willVisit.push({x, y - 1});
            n++;
        }
        if (x != 11 && checked[x + 1][y] == 0 && ch == arr[x + 1][y])
        {
            checked[x + 1][y] = 3;
            willVisit.push({x + 1, y});
            n++;
        }
        if (y != 5 && checked[x][y + 1] == 0 && ch == arr[x][y + 1])
        {
            checked[x][y + 1] = 3;
            willVisit.push({x, y + 1});
            n++;
        }
    }
    if (n >= 4)
    {
        for (int i = 0; i < 12; i++)
        {
            for (int j = 0; j < 6; j++)
            {
                // cout<<checked[i][j]<<"\n";
                if (checked[i][j] == 3)
                {
                    checked[i][j] = 1;
                    arr[i][j] = '.';
                }
            }
        }
        for (int j = 0; j < 6; j++)
        {
            string s = "";
            for (int i = 11; i >= 0; i--)
            {
                if (arr[i][j] != '.')
                {
                    s = s + arr[i][j];
                    arr[i][j] = '.';
                }
            }
            for (int i = 0; i < s.length(); i++)
            {
                arr[11 - i][j] = s[i];
            }
        }
        return true;
    }
    else
    {
        for (int i = 0; i < 12; i++)
        {
            for (int j = 0; j < 6; j++)
            {
                if (checked[i][j] == 3)
                {
                    checked[i][j] = 2;
                }
            }
        }
        return false;
    }
}
bool pang()
{
    resetChecked();
    bool didPang = false;
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            if (checked[i][j] == 0 && arr[i][j] != '.')
            {
                if (checkNbd(i, j))
                {
                    didPang = true;
                }
            }
        }
    }
    return didPang;
}
bool prnt()
{
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            if (arr[i][j] != '.')
                return true;
        }
    }
    return false;
}
int main()
{
    int answer = 0;
    for (int i = 0; i < 12; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < 6; j++)
        {
            arr[i][j] = s[j];
        }
    }
    // cout<<checkNbd(11,0);
    while (1)
    {
        if (!pang())
            break;
        answer++;
    }
    cout << answer;
    return 0;
}