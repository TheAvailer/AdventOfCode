import java.util.concurrent.Callable;

public class FishCore implements Callable<Integer> {

    private final String startData;

    public FishCore(String startData) {
        this.startData = startData;

    }


    @Override
    public Integer call() throws Exception {
        String workData = startData;

        for (int i = 0; i < 256; i++) {
            String children = "";
            String newWorkData = "";
            for (String f : workData.split(",")) {
                if (f.isBlank()) continue;
                int fish = Integer.parseInt(f);
                if (fish == 0) {
                    children += "8,";
                    fish = 6;
                } else {
                    fish--;
                }
                newWorkData += fish + ",";

            }
            workData = newWorkData + children;
        }

        return workData.length() / 2;
    }
}
