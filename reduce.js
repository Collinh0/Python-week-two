const myArray = [ 20, 30, 40, 50,  10, 60, 70, 80, 90];

const maxNum = myArray.reduce((acc, current) => {
  return current > acc ? current : acc;
}, myArray[4]);

console.log(maxNum);
