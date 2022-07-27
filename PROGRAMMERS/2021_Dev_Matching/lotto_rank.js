function rank(num) {
  if (num >= 2) {
    return 7 - num;
  } else {
    return 6;
  }
}

function solution(lottos, win_nums) {
  let collect = 0;
  let zeros = 0;
  for (let i = 0; i < lottos.length; i++) {
    if (lottos[i] === 0) {
      zeros += 1;
    } else {
      if (win_nums.includes(lottos[i])) {
        collect += 1;
      }
    }
  }

  var answer = [];
  answer.push(rank(collect + zeros));
  answer.push(rank(collect));
  return answer;
}
