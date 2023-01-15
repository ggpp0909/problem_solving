import java.util.Scanner;

public class Main_3003 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] correctSet = new int[] {1, 1, 2, 2, 2, 8};

        for (int i = 0; i < 6; i++) {
            int cnt = sc.nextInt();
            System.out.print(Integer.toString(correctSet[i] - cnt) + " ");
        }
    }
}
