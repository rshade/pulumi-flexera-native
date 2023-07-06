import * as flexera-native from "@pulumi/flexera-native";

const random = new flexera-native.Random("my-random", { length: 24 });

export const output = random.result;