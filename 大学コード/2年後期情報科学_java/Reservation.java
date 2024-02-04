public class Reservation{
    int seat[][];

    public Reservation(int n, int m){
        seat = new int[n][m];
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                seat[i][j]=-1;
            }
        }
    }

    boolean reserve(int id, int num){ //変更箇所
        int x_coordinate = (int)(Math.random()*15);
        int y_coordinate = (int)(Math.random()*(7-num));

        for(int i = 0; i < num; i++){
            if(seat[y_coordinate + i][x_coordinate] == -1){
            }else{
                return false;
            }
        }

        for(int i = 0; i < num; i++){
            seat[y_coordinate + i][x_coordinate] =1;
        }
        return true;
    }

    void printSeat(){  //変更箇所
        int sum = 0;
        for(int i=0;i<seat.length;i++){
            for(int j=0;j<seat[i].length;j++){
                System.out.print(seat[i][j]+"\t");
                if(seat[i][j]==1){sum = sum + 1;}
            }
System.out.println();
        }
        System.out.println("sum =" + sum);
    }

    public void res(){  //追加箇所
        int id = Passengers.id;
        Reservation rs = Passengers.rs;
        synchronized(this){
            for(int i=0;i<10;i++){
                int num = (int)(Math.random()*6+1);
                if(rs.reserve(id, num)){
                    System.out.println("ID:"+id+"  reserved "+num+" seats. "\
 );} }
        }
    }

    public static void main(String args[]){
        int thread_num = 5;
        Reservation rs = new Reservation(6,15);
        Passengers ps[] = new Passengers[thread_num];
        for(int i=0;i<thread_num;i++){
            ps[i] = new Passengers(i,rs);
        }
        for(int i=0;i<thread_num;i++){
            try{
                ps[i].join();
            }catch(InterruptedException e){
            }
        }
        rs.printSeat();
    }
}

class Passengers extends Thread{
static int id;
    static Reservation rs;
    public Passengers(int n, Reservation rs){
        this.id = n;
        this.rs = rs;
        this.start();
    }
    public void run(){ //resメソッドに記述を移動した
        rs.res();
    }
}
