#include <iostream>
using namespace std;

int arr[1000001];
int sz = 0;
int n;
int findindex(int x)
{
    int index = -1;
    if (sz == 0)
        return -1;
    if (arr[sz - 1] < x)
    {
        return -1;
    }
    else
    {
        int a = 0;
        int b = sz - 1;
        int mid = (a + b) / 2;
        while (1)
        {
            if (a == b)
            {
                index = a;
                break;
            }
            if (a + 1 == b)
            {
                if (arr[a] >= x)
                {
                    index = a;
                    break;
                }
                else
                {
                    index = b;
                    break;
                }
            }

            if (arr[mid] < x)
            {
                a = mid;
                mid = (a + b) / 2;
            }
            else if (arr[mid] > x)
            {
                b = mid;
                mid = (a + b) / 2;
            }
            else if (arr[mid] == x)
            {
                index = mid;
                break;
            }
        }
    }
    return index;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    int x;
    int index = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        index = findindex(x);

        if (index == -1)
        {
            arr[sz] = x;
            sz++;
        }

        else
            arr[index] = x;
        // for(int i=0;i<sz;i++)cout<<arr[i]<<" ";
        // cout<<"\n";
    }

    cout << sz;
}