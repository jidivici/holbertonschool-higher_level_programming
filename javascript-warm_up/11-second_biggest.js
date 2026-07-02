#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const ints = args.map((x) => parseInt(x));
  const max = Math.max(...ints);
  const idx = ints.indexOf(max);
  ints.splice(idx, 1);
  console.log(Math.max(...ints));
}
