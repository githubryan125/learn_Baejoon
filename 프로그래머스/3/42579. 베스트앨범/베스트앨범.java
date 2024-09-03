import java.util.*;

public class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> genrePlayCount = new HashMap<>();
        Map<String, List<int[]>> genreSongs = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            genrePlayCount.put(genre, genrePlayCount.getOrDefault(genre, 0) + play);
            
            List<int[]> songs = genreSongs.getOrDefault(genre, new ArrayList<>());
            songs.add(new int[]{i, play});
            genreSongs.put(genre, songs);
        }
        
        List<Map.Entry<String, Integer>> genreList = new ArrayList<>(genrePlayCount.entrySet());
        genreList.sort((a, b) -> b.getValue() - a.getValue());
        
        List<Integer> result = new ArrayList<>();
        
        for (Map.Entry<String, Integer> entry : genreList) {
            String genre = entry.getKey();
            List<int[]> songs = genreSongs.get(genre);
            
            songs.sort((a, b) -> {
                if (b[1] != a[1]) {
                    return b[1] - a[1];
                } else {
                    return a[0] - b[0];
                }
            });
            
            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                result.add(songs.get(i)[0]);
            }
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}
