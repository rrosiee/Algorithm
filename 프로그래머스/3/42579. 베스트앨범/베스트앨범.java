import java.util.*;
import java.util.stream.Stream;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        // Variables
        HashMap<String, Integer> playMap = new HashMap<>();
        HashMap<String, ArrayList<int[]>> genreMap =  new HashMap<>();
        
        // 1. genre별 총 play수와 genre별 index의 play수 HahMap 생성
        for (int i=0; i<genres.length; i++) {
            
            // Genre별 총 Play수 계산
            playMap.put(genres[i], playMap.getOrDefault(genres[i], 0) + plays[i]);
            
            // Genre별 index와 play 수
            if (!genreMap.containsKey(genres[i])) {
                genreMap.put(genres[i], new ArrayList<>());
            }
            
            genreMap.get(genres[i]).add(new int[]{i, plays[i]});
        }
        
        // 총 재생횟수가 많은 장르 순으로 내림차순 정렬
        ArrayList<Integer> answer = new ArrayList<>();
        Stream<Map.Entry<String, Integer>> sortedGenres = playMap.entrySet().stream().sorted((o1, o2) -> Integer.compare(o2.getValue(), o1.getValue()));
        sortedGenres.forEach(entry -> {
            Stream<int[]> sortedSongs = genreMap.get(entry.getKey()).stream().sorted((o1, o2) -> Integer.compare(o2[1], o1[1])).limit(2);
            sortedSongs.forEach(song -> answer.add(song[0]));
            }
        );
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}