import java.util.ArrayList;
import java.util.List;

public class Day02 {
    private class NounVerb {
        int noun;
        int verb;

        public int getAnswer() {
            return this.noun * 100 + verb;
        }
    }

    private NounVerb findNounVerb(List<Integer> intCode, int expectedAnswer) {
        NounVerb nv = new NounVerb();

        for (int n = 0; n <= 99; n++) {
            for (int v = 0; v <= 99; v++) {
                List<Integer> ic = new ArrayList<>(intCode);
                if (executeIntCode(ic, n, v).get(0) == expectedAnswer) {
                    nv.noun = n;
                    nv.verb = v;
                    return nv;
                }
            }
        }
        return nv;
    }

    private List<Integer> executeIntCode(List<Integer> intCode, int noun, int verb) {
        intCode.set(1, noun);
        intCode.set(2, verb);
        int optCodePosition = 0;

        while (intCode.size() > optCodePosition) {
            int optCode = intCode.get(optCodePosition);
            switch (optCode) {
                default:
                    throw new RuntimeException(String.valueOf(optCode));
                case 99:
                    return intCode;
                case 1:
                    intCode.set(
                            intCode.get(optCodePosition + 3),
                            intCode.get(intCode.get(optCodePosition + 1)) + intCode.get(intCode.get(optCodePosition + 2))
                    );
                    break;
                case 2:
                    intCode.set(
                            intCode.get(optCodePosition + 3),
                            intCode.get(intCode.get(optCodePosition + 1)) * intCode.get(intCode.get(optCodePosition + 2))
                    );
                    break;
            }
            optCodePosition += 4;
        }

        return intCode;
    }

    public static void main(String[] args) {
        Day02 solution = new Day02();
        // List<Integer> intCode = new ArrayList<>(List.of(1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50));
        List<Integer> intCode = new ArrayList<>(List.of(1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 19, 9, 23, 1, 23, 9, 27, 1, 10, 27, 31, 1, 13, 31, 35, 1, 35, 10, 39, 2, 39, 9, 43, 1, 43, 13, 47, 1, 5, 47, 51, 1, 6, 51, 55, 1, 13, 55, 59, 1, 59, 6, 63, 1, 63, 10, 67, 2, 67, 6, 71, 1, 71, 5, 75, 2, 75, 10, 79, 1, 79, 6, 83, 1, 83, 5, 87, 1, 87, 6, 91, 1, 91, 13, 95, 1, 95, 6, 99, 2, 99, 10, 103, 1, 103, 6, 107, 2, 6, 107, 111, 1, 13, 111, 115, 2, 115, 10, 119, 1, 119, 5, 123, 2, 10, 123, 127, 2, 127, 9, 131, 1, 5, 131, 135, 2, 10, 135, 139, 2, 139, 9, 143, 1, 143, 2, 147, 1, 5, 147, 0, 99, 2, 0, 14, 0));
        NounVerb answer = solution.findNounVerb(intCode, 19690720);
        System.out.println(answer.getAnswer());
    }
}