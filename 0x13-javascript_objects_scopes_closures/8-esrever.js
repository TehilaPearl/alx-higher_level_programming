#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  const revList = [];
  for (i = (list.length - 1); i >= 0; i--) {
    revList.push(list[i]);
  }
  return (revList);
};
