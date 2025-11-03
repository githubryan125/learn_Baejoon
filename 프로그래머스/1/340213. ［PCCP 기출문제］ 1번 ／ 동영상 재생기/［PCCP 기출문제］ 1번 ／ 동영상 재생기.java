class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        // 문자열을 초 단위로 변환하는 함수
        int videoLen = toSec(video_len);
        int position = toSec(pos);
        int opStart = toSec(op_start);
        int opEnd = toSec(op_end);

        for (String command : commands) {
            // 오프닝 구간이면 건너뛰기
            if (position >= opStart && position <= opEnd) {
                position = opEnd;
            }

            if (command.equals("next")) {
                position += 10;
            } else if (command.equals("prev")) {
                position -= 10;
            }

            // 범위 조정: 0 ~ videoLen
            if (position < 0) position = 0;
            if (position > videoLen) position = videoLen;

            // 오프닝 구간이면 다시 한 번 점프
            if (position >= opStart && position <= opEnd) {
                position = opEnd;
            }
        }

        return toTime(position);
    }

    // "mm:ss" → 초 단위로 변환
    private int toSec(String time) {
        String[] t = time.split(":");
        int min = Integer.parseInt(t[0]);
        int sec = Integer.parseInt(t[1]);
        return min * 60 + sec;
    }

    // 초 단위 → "mm:ss" 변환
    private String toTime(int totalSec) {
        int min = totalSec / 60;
        int sec = totalSec % 60;
        return String.format("%02d:%02d", min, sec);
    }
}
