#!/usr/bin/node
exports.converter = function (base) {
  return function (s) {
    return s.toString(base);
  };
};
