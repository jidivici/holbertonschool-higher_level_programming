#!/usr/bin/node

const nb_args = process.argv.length - 2;

if (nb_args === 0) {
  console.log('No argument');
} else if (nb_args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
