import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class day6 {

    public static void main(String[] args) throws InterruptedException {
        String test = "3,4,3,1,2";
        //String data = "1,1,1,1,2,1,1,4,1,4,3,1,1,1,1,1,1,1,1,4,1,3,1,1,1,5,1,3,1,4,1,2,1,1,5,1,1,1,1,1,1,1,1,1,1,3,4,1,5,1,1,1,1,1,1,1,1,1,3,1,4,1,1,1,1,3,5,1,1,2,1,1,1,1,4,4,1,1,1,4,1,1,4,2,4,4,5,1,1,1,1,2,3,1,1,4,1,5,1,1,1,3,1,1,1,1,5,5,1,2,2,2,2,1,1,2,1,1,1,1,1,3,1,1,1,2,3,1,5,1,1,1,2,2,1,1,1,1,1,3,2,1,1,1,4,3,1,1,4,1,5,4,1,4,1,1,1,1,1,1,1,1,1,1,2,2,4,5,1,1,1,1,5,4,1,3,1,1,1,1,4,3,3,3,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,5,1,3,1,4,3,1,3,1,5,1,1,1,1,3,1,5,1,2,4,1,1,4,1,4,4,2,1,2,1,3,3,1,4,4,1,1,3,4,1,1,1,2,5,2,5,1,1,1,4,1,1,1,1,1,1,3,1,5,1,2,1,1,1,1,1,4,4,1,1,1,5,1,1,5,1,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,3,2,4,1,1,2,1,1,3,2";

        ExecutorService es = Executors.newFixedThreadPool( 5);
        List<Future> resultList = new ArrayList<>();
        for (String workData : test.split(","))
        {
            resultList.add(es.submit(new FishCore(workData)));

        }

        es.awaitTermination(5, TimeUnit.SECONDS);

        int fishes = 0;
        for (int i = 0; i < resultList.size(); i++){
            Future<Integer> result = resultList.get(i);
            Integer number = null;
            try {
                number = result.get();
            } catch (InterruptedException e){
                e.printStackTrace();
            }   catch (ExecutionException e){
                e.printStackTrace();
            }
            fishes += number;
        }

        System.out.println(fishes);

        es.shutdown();
    }

}





