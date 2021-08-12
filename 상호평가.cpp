#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<vector<int>> scores) {
    string answer = "";
    for (int i=0;i<scores.size();i++) {
        vector<int> student;
        for (int j=0;j<scores.size();j++) {
            if (i!=j) student.push_back(scores[j][i]); //자기 자신 제외한 점수 push!
        }

        int max = *max_element(student.begin(), student.end()); //그 중 가장 큰 값
        int min = *min_element(student.begin(), student.end()); //그 중 가장 작은 값
        if (min <= scores[i][i] && scores[i][i] <= max)
            student.push_back(scores[i][i]); //유일한 최고점, 최저점이 아니면 push

        //평균 계산
        int avg = 0;
        for (int i=0;i<student.size();i++) avg+=student[i];
        avg/=student.size();
        //결과 입력
        if (90 <= avg) answer += 'A';
        else if(80 <= avg) answer += 'B';
        else if (70 <= avg) answer += 'C';
        else if (50 <= avg) answer += 'D';
        else answer += 'F';
    }
    return answer;
}
