#include <iostream>
using namespace std;
int mts[100001];
int index = 0; // 원소의 개수
void push(int x)
{
    mts[index] = x;
    index++;
}
int pop()
{
    if (index == 0)
        return -1;
    index -= 1;
    return mts[index];
}
int top()
{
    if (index == 0)
        return -1;
    return mts[index - 1];
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
    string s;
    bool isvps = true;
    while (1)
    {
        getline(cin, s);
        if (s == ".")
            return 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] == '(')
            {
                push(1);
            }
            else if (s[i] == ')')
            {
                if (pop() != 1)
                    isvps = false;
            }
            else if (s[i] == '[')
            {
                push(2);
            }
            else if (s[i] == ']')
            {
                if (pop() != 2)
                    isvps = false;
            }

            if (s[i] == '.')
            {
                if (index > 0)
                    isvps = false;
                if (isvps)
                    cout << "yes\n";
                else
                    cout << "no\n";
                index = 0;
                isvps = true;
            }
        }
    }
}