import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        Set<String> usedWords = new HashSet<>();
        usedWords.add(words[0]);
        char lastChar = words[0].charAt(words[0].length() - 1);

        for (int i = 1; i < words.length; i++) {
            String word = words[i];

            // 규칙 위반: 앞 글자 불일치 or 1글자 or 중복 단어
            if (word.charAt(0) != lastChar || word.length() == 1 || usedWords.contains(word)) {
                answer[0] = (i % n) + 1; // 사람 번호
                answer[1] = (i / n) + 1; // 차례
                break;
            }

            usedWords.add(word);
            lastChar = word.charAt(word.length() - 1);
        }

        return answer;
    }
}
