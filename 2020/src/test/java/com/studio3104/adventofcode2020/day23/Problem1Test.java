package com.studio3104.adventofcode2020.day23;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

class Problem1Test {
    static Stream<Arguments> argumentsProvider() {
        return Stream.of(
                Arguments.of(new int[]{3, 8, 9, 1, 2, 5, 4, 6, 7}, 67_384_529)
        );
    }

    @ParameterizedTest
    @MethodSource("argumentsProvider")
    void getResult(int[] input, int expected) {
        int actual = Problem1.getResult(input);
        Assertions.assertEquals(expected, actual);
    }
}
