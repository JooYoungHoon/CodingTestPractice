import java.util.*;

public class BOJ10994 {

    static int n;
    static ArrayList<String> list = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        list.add("*");

        for(int a = 1; a < n; a++) {
            for(int i = 0 ; i < list.size(); i++) {
                String temp = list.get(i);
                list.remove(i);
                list.add(i, "* "+temp+" *");
            }

            String temp = list.get(0);
            String empty = "";

            for(int i = 0; i < temp.length()-2; i++) {
                empty += " ";
            }
            list.add("*"+empty+"*");
            temp = "";

            for(int i = 0; i < empty.length()+2; i++) {
                temp += "*";
            }

            list.add(temp);
        }

        for(int i = list.size()-1; i > 0; i--) {
            System.out.println(list.get(i));
        }

        for(int i = 0 ; i < list.size(); i++) {
            System.out.println(list.get(i));
        }

    }

}