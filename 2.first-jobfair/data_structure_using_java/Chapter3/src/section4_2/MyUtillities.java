package section4_2;

public class MyUtillities {
	// genericÇÑ bubble sort
	public static void bubbleSort(Comparable [] data, int size) {
		for (int i=size; i>0; i--) {
			for (int j=0; j<i; j++) {
				if ( data[j].compareTo(data[j+1]) > 0) {
					Comparable tmp = data[j];
					data[j] = data[j+1];
					data[j+1] = tmp;
				}
			}
		}
	}
}
