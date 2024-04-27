#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int num;
vector<pair<int, int>> n;
vector<int> max_l;
int main()
{
    cin >> num;
    for (int i = 0; i < num; i++)
    {
        int x, y;
        cin >> x >> y;
        n.push_back({x, y});
    }
    sort(n.begin(), n.end());
    max_l.push_back(n.at(0).second);
    for (int i = 1; i < n.size(); i++)
    {
        int x = n.at(i).second;
        for (int j = 0; j < max_l.size(); j++)
        {
            if (x < max_l.at(j))
            {
                max_l.at(j) = x;
                break;
            }
        }
        if (x > max_l.at(max_l.size() - 1))
            max_l.push_back(x);
    }
    cout << num - max_l.size();
    return 0;
}