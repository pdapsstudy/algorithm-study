#include <iostream>
using namespace std;
int mfs[10001]; // myFirstStack 이라는 뜻 ~ 헤헤
int index = 0;  // 원소의 개수
void push(int x)
{
    mfs[index] = x;
    index++;
}
int pop()
{
    if (index == 0)
        return -1;
    index -= 1;
    return mfs[index];
}
int top()
{
    if (index == 0)
        return -1;
    return mfs[index - 1];
}
int empty()
{
    if (index == 0)
        return 1;
    else
        return 0;
}
int size()
{
    return index;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    string s;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        if (s[1] == 'u')
        {
            int a;
            cin >> a;
            push(a);
        }
        else if (s[0] == 't')
        {
            cout << top() << "\n";
        }
        else if (s[0] == 'e')
        {
            cout << empty() << "\n";
        }
        else if (s[0] == 'p')
        {
            cout << pop() << "\n";
        }
        else
        {
            cout << size() << "\n";
        }
    }
    return 0;
}