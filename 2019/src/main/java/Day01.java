import java.util.List;

public class Day01 {
    private int calculateFuel(int mass) {
        return (int) Math.floor((double) mass / 3) - 2;
    }

    private int calculateFuels(List<Integer> masses) {
        // Wanna implement using REDUCE or something cool...
        int answer = 0;
        for (int mass: masses) {
            // This is only for Part 1
            // answer += calculateFuel(mass);
            while (true) {
                mass = calculateFuel(mass);
                if (mass <= 0) {
                    break;
                }
                answer += mass;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Day01 solution = new Day01();
        List<Integer> masses = List.of(50962, 126857, 127476, 136169, 62054, 116866, 123235, 147126, 146767, 140795, 54110, 106452, 98413, 114925, 141914, 54864, 120093, 118166, 81996, 143924, 145941, 96950, 126488, 85764, 111438, 63278, 147558, 128982, 123857, 58646, 80757, 98260, 97143, 136609, 99349, 63167, 142129, 144645, 97212, 70162, 98044, 125931, 103859, 67890, 67797, 79263, 134255, 130303, 73367, 103091, 97315, 74892, 82311, 51157, 79802, 138401, 108423, 63111, 61441, 102862, 53184, 125543, 147413, 117762, 106771, 115805, 66424, 85851, 53101, 82736, 136768, 130745, 140135, 101770, 55349, 143419, 60108, 84990, 91544, 75240, 92709, 134369, 140901, 59910, 63641, 54966, 104671, 71950, 60358, 127289, 147362, 70799, 82870, 108630, 53450, 106888, 129843, 53227, 58758, 137751);
        int answer = solution.calculateFuels(masses);
        System.out.println(answer);
    }
}