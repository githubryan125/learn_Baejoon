import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < operations.length; i++) {
            char C = operations[i].charAt(0);
            if (C == 'I') {
                int num = Integer.parseInt(operations[i].substring(2));
                list.add(num);
                Collections.sort(list);
            } else if (C == 'D') {
                if (operations[i].charAt(2) == '1' && !list.isEmpty()) {
                    list.remove(list.size() - 1);
                } else if (operations[i].charAt(2) == '-' && !list.isEmpty()) {
                    list.remove(0);
                }
            }
        }
        if (list.isEmpty()) {
            answer[0] = 0;
            answer[1] = 0;
        } else {
            answer[0] = list.get(list.size() - 1); 
            answer[1] = list.get(0);
        }
        
        return answer;
    }
}
