#include <iostream>
#include <string>

using namespace std;

class RunLengthEncode {
public:
    string encode(const string& s) {
        string result;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (j < s.length() && s[j] == s[i]) {
                j++;
            }
            int count = j - i;
            if (count >= 5) {
                result += "/";
                result += to_string(count);
                result += s[i];
            } else {
                result += s.substr(i, count);
            }
            i = j;
        }
        return result;
    }
};

int main() {
    RunLengthEncode rle;
    string input = "aaaaa";
    cout << rle.encode(input) << endl;
    return 0;
}
