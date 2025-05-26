import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) return 0;

        Queue<WordNode> queue = new LinkedList<>();
        boolean[] visited = new boolean[words.length];

        queue.add(new WordNode(begin, 0));

        while (!queue.isEmpty()) {
            WordNode current = queue.poll();

            if (current.word.equals(target)) {
                return current.step;
            }

            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && canConvert(current.word, words[i])) {
                    visited[i] = true;
                    queue.offer(new WordNode(words[i], current.step + 1));
                }
            }
        }

        return 0;
    }

    private boolean canConvert(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) count++;
            if (count > 1) return false;
        }
        return count == 1;
    }

    class WordNode {
        String word;
        int step;

        WordNode(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }
}
