class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        int big =0;
        int index=0;
        for (int i=0; i<array.length;i++){
            if (array[i]>big){
                index =i;
                big = array[i];
            }
        }
        answer[0]=big;
        answer[1]=index;
        return answer;
    }
}