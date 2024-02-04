public class Sort{
    private int array[];
    public Sort(int n){
        array = new int[n];
        for(int i=0;i<n;i++){
            array[i] = (int)(Math.random()*Integer.MAX_VALUE);
        }
        //ここからソート呼び出し
        long start = System.currentTimeMillis();
        QuickSort qs = new QuickSort(array);
        array = qs.getArray();
        //printArray(array); //配列表示
        long end = System.currentTimeMillis();
        System.out.println("sort?: "+sortCheck(array)+
                           ", Processing time: "+(end-start)+"ms");
    }

    /** ソートチェック */
    public static boolean sortCheck(int array[]){
        for(int i=0;i<array.length-1;i++){
            if(array[i]>array[i+1])return false;
        }
        return true;
    }
    
    /** 確認用の配列表示メソッド */
    public static void printArray(int array[]){
        for(int i=0;i<array.length;i++){
            System.out.print(array[i]+" ");
        }
        System.out.println();
    }

    public static void main(String args[]){
        new Sort(1000000);
    }
}

class QuickSort{
    private int array[];

    QuickSort(int[] n){
        array = n;
        SubQuickSort q = new SubQuickSort(array , 0, array.length-1);
    }

    /** ソート コンストラクタから自動で実行される */
    

    /** ソート結果を得るメソッド */
    public int[] getArray(){
	return array;
    }
}
class SubQuickSort extends Thread{
    public int array2[];
    public int left, right;
    static int NumOfThread;
    public SubQuickSort(int[] na, int left, int right){
	array2 = na;
	this.left = left;
	this.right = right;
	NumOfThread++;
	this.start();
	try{
	    this.join();
	}catch(InterruptedException e){}
    }
    public void run(){
	sort(array2, 0, array2.length-1);
    }
    private void sort(int[] d, int left, int right){
        if(left >= right){return;}

        int p = d[(left+right)/2];
        int l = left, r = right, a;

        while(l<=r) {
            while(d[l] < p) { l++; }
            while(d[r] > p) { r--; }

	    if (l<=r) {
                a = d[l]; d[l] = d[r]; d[r] = a;
                l++; r--;
            }
        } 
	if(this.NumOfThread < 4){
	    //if(false){
		 SubQuickSort q1 = new SubQuickSort(d, left, r);
	    //sort(d, left, r); //ぴぼットより左側をクイックソート
	    SubQuickSort q2 = new SubQuickSort(d, l, right);
	    //sort(d, l, right); // ピボットより右側をクイックソート
	    try{
		q1.join();
		q2.join();
	    }catch(InterruptedException e){}
	}else{
	    sort(d, left, r);
	    sort(d, l, right);
	}
    }


}
