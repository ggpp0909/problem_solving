import java.util.Scanner;

public class Main_2525 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int M = sc.nextInt();
        int C = sc.nextInt();

        // 현재시간 분단위로 변환
        int curTimeMin = H * 60 + M;

        // 현재시간에 요리시간 더하기
        int afterCook = curTimeMin + C;

        // 시, 분으로 나누기
        int ansMin = afterCook % 60;
        int ansHour = (afterCook / 60) % 24;
        System.out.println(ansHour + " " + ansMin);
    }
}
