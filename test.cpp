//c++ -O2 primes.cpp -lprimesieve

#include <primesieve.hpp>
#include <iostream>
#include <vector>

int main()
{
  // store the primes below 1000
  std::vector<int> primes;
  primesieve::generate_primes(1000, &primes);

  primesieve::iterator it;
  uint64_t prime = it.next_prime();

  // iterate over the primes below 10^6
  int cnt=0;
  for (; prime < 100; prime = it.next_prime())
    cnt++;
    std::cout << prime << std::endl;
  c
  return 0;
}