package level_1;

import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        String temp = "";

        Arrays.sort(participant);
        Arrays.sort(completion);

        int i;
        for(i=0;i <completion.length;i++) {
            if(!participant[i].equals(completion[i])) {
                return  participant[i];
            }
        }

        return participant[i];
    }
}

public class One {
    public static void main(String[] args) {

    }
}
