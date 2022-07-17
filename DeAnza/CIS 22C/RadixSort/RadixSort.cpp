/*
 * RadixSort.cpp
 *
 *  Created on: Jul 12, 2022
 *      Author: yannik
 */


#include "Linkedlist.h"
#include <vector>

int getMax(int A[], int n)
{
	int max = A[0];
	for (int i = 1; i < n; i++)
		if (A[i] > max)
			max = A[i];
	return max;
}

void RadixSort(int A[], int r, int n) {

  int maxval = getMax(A,n);
  Queue<int> bins[r];

  for (int rtok = 1; maxval/rtok > 0; rtok *= r) {
	// until we reach the number of digits in maxval

    // Push current entry into queue at index (A[j]/rtok)%r in bins
    // i.e. this is the value corresponding to the ith digit
    for (int j = 0; j < n; j++) {
		int curr = A[j];
		int digit = (curr/rtok) % r;
		bins[digit].Push(curr);
		// int digit = (A[j]/rtok) % r;
		// bins[digit].Push(A[j])
	}

    // Now go through the bins and create a new list ordered by these
    // bin entries
	int m=0;
    for (int k = 0; k < r; k++) {
    	// look at bins[k] and check if empty
    	if (!bins[k].IsEmpty()){
    		while (bins[k].GetLength() > 0){
				//bins[k].PrintQueue(); to check if bins updated correctly
    			int elt=bins[k].Pop();
				// update the array A
    			A[m]=elt;
				m++;
    		}
    	}
    }

  }
}

int main()
{
	int count = 100;
	int list[count];
	for (int x = 0; x < count; x++)
	{
		int rnumber = rand() % 10000 + 1;
		list[x]=rnumber;
		//cout << rnumber << "\t";
	}
	//cout << endl;

	//for (vector<int>::iterator it=list.begin(); it != list.end(); it++){
	//	cout<< *it << ", ";
	//}

	//for (int x = 0; x < count; x++){
	//	cout << list[x] << " ";
	//}

	RadixSort(list,10,count);

	for (int x = 0; x < count; x++){
		cout << list[x] << " ";
	}
	cout << endl;

	//cout << getMax(list, count);
}
