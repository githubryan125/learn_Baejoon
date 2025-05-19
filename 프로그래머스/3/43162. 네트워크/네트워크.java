class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visit = new boolean[n];
        int answer = 0;
        
        for(int i=0;i<computers.length;i++){
            if(!visit[i]){
                dfs(i,visit,computers);
                answer+=1;
            }
        }
        return answer;
    }
    private void dfs(int now, boolean[] visit, int[][] computers){
        visit[now]=true;
        for(int i=0;i<computers.length;i++){
            if(computers[now][i]==1 && !visit[i]){
                dfs(i,visit,computers);
            }
        }
    }
}