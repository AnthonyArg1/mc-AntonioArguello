Import java.util.HashSet;
Import java.util.Scanner;

package Taller;


public class Taller1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashSet<Integer> conjuntoA = new HashSet<>();
		
		for (int i = 0; i < 5; i++){
			System.out.print("Un número: ");
			int aux = sc.nextInt();

			conjuntoA.add(aux);
		}

		System.out.println("A = " + conjuntoA);

		for (int elemento : conjuntoA){
			System.out.println(elemento);
		}
	
		System.out.println("Conjunto B");
		HashSet<Integer> conjuntoB = new HashSet<>();
		for (int i = 0; i < 5; i++) {
			System.out.print("Un número : ");
			int aux = sc.nextInt();

			conjuntoB.add(aux);
		}
		

		System.out.println("B = " + conjuntoB);

		//union
		HashSet<Integer> conjuntoUnion = new HashSet<>();
		for (int elemento : conjuntoA){
			conjuntoUnion.add(elemento);
		}
		for (int elemento : conjuntoB){
			conjuntoUnion.add(elemento);
		}

		System.out.println(" ");

	}

}