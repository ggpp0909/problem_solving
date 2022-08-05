var isPalindrome = function (head) {
  console.log(head);
  const temp = [...head];
  const temp2 = head.reverse();
  return JSON.stringify(temp) === JSON.stringify(temp2);
};
// ES6 버전
