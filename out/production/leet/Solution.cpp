#include <iostream>
#include <vector>
#include <cassert>
#define NDEBUG

using namespace std;

class Solution
{
public:
    int doA()
    {
        return 20;
    }

    vector<int> getMaximumXor(vector<int> &nums, int maximumBit)
    {

        int length = nums.size();
        vector<int> result(length, 0);
        int total_xor = 0;

        int extrema = (1 << maximumBit) - 1;

        for (size_t i = 0; i < length; i++)
        {

            int element = nums[i];
            total_xor = total_xor ^ element;
            result[length - i - 1] = extrema - total_xor;
        }

        return result;
    }
};

int main()
{

    Solution n;
    vector<int> in = {0, 1, 1, 3}; // cout << vec;
    vector<int> out = {0, 3, 2, 3};

    auto ans = n.getMaximumXor(in, 2);
    // for (int element : ans)
    // {
    // cout << element << " ";
    // }
    assert(ans == out);

    return 0;
}
