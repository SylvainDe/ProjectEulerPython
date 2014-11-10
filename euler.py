#! /usr/bin/python3
# vim: set tabstop=4 shiftwidth=4 expandtab :
# Generated by letscode

"""Project Euler solutions"""
import string
import math
import itertools
from prime import prime_factors_list, sieve, nb_divisors, yield_primes
from prime import primes_up_to, nb_prime_divisors, totient, divisors_sieve
from prime import is_prime, prime_divisors_sieve, mult
from functions import fibo, lcmm, yield_pythagorean_triples_of_peri, gcd
from functions import Tn, Pn, Hn


def euler1(lim=1000):
    """Solution for problem 1."""
    # could use sum formula here
    return sum(i for i in range(lim) if i % 3 == 0 or i % 5 == 0)


def euler2(lim=4000000):
    """Solution for problem 2."""
    s = 0
    for f in fibo(1, 2):
        if f > lim:
            return s
        if f % 2 == 0:
            s += f


def euler3(n=600851475143):
    """Solution for problem 3."""
    return prime_factors_list(n)[-1]


def euler4(l=3):
    """Solution for problem 4."""
    # simple optimisation would be an early break
    return max(n for n in (i * j for i, j in itertools.combinations(range(10 ** (l - 1), 10 ** l), 2)) if str(n) == str(n)[::-1])


def euler5(lim=20):
    """Solution for problem 5."""
    return lcmm(*range(1, lim + 1))


def euler6(lim=100):
    """Solution for problem 6."""
    # could use sum formula here
    numbers = range(1, lim + 1)
    sum_ = sum(numbers)
    return sum_ * sum_ - sum(i * i for i in numbers)


def nth(iterable, n, default=None):
    """Returns the nth item or a default value.
    From http://stackoverflow.com/questions/12007820/better-ways-to-get-nth-element-from-an-unsubscriptable-iterable ."""
    return next(itertools.islice(iterable, n, None), default)


def euler7(n=10001):
    """Solution for problem 7."""
    return nth(yield_primes(), n - 1)


def euler8(l=13):
    """Solution for problem 8."""
    # Too lazy for optimisations
    n = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    return max(mult(int(c) for c in s) for s in (n[i:i + l] for i in range(len(n))))


def euler9(p=1000):
    """Solution for problem 9."""
    for a, b, c in yield_pythagorean_triples_of_peri(p):
        return a * b * c


def euler10(lim=2000000):
    """Solution for problem 10."""
    return sum(primes_up_to(lim))


def euler12(nb_div=500):
    """Solution for problem 12."""
    t = 0
    for i in itertools.count(1):
        t += i
        if nb_divisors(t) >= nb_div:
            return t


def euler15(col=20, row=20):
    """Solution for problem 15."""
    nb_routes = [[0] * (row + 1) for i in range(col + 1)]
    nb_routes[0][0] = 1
    for i in range(col + 1):
        for j in range(row + 1):
            if i:
                nb_routes[i][j] += nb_routes[i - 1][j]
            if j:
                nb_routes[i][j] += nb_routes[i][j - 1]
    return nb_routes[-1][-1]


def sum_digit(n):
    return sum(int(c) for c in str(n))


def euler16(n=1000):
    """Solution for problem 16."""
    return sum_digit(2 ** n)


def euler19():
    """Solution for problem 19."""
    day = 2  # Tuesday 1 Jan 1901
    nb_days = 7
    freq = [0] * nb_days
    months = [nb % nb_days for nb in (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)]
    for year in range(1901, 2001):
        for i, month in enumerate(months):
            freq[day] += 1
            day = (day + month + (1 if (i == 1 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))) else 0)) % nb_days
    return freq[0]


def euler20(n=100):
    """Solution for problem 20."""
    return sum_digit(math.factorial(n))


def euler21(lim=10000):
    """Solution for problem 21."""
    sum_div = [sum(l) for l in divisors_sieve(lim)]
    return sum(
        s + i
        for i, s in enumerate(sum_div)
        if s < i and sum_div[s] == i)


def euler22(f='p022_names.txt'):
    """Solution for problem 22."""
    with open(f) as file_:
        return sum((i + 1) * sum(1 + ord(c) - ord('A') for c in name)
                   for i, name in enumerate(sorted(''.join(file_.readlines()).replace('"', '').split(','))))


def euler23(lim=28123):
    """Solution for problem 23."""
    abun = [i > 0 and sum(l) > i for i, l in enumerate(divisors_sieve(lim))]
    return sum(
        n for n in range(lim)
        if not any(i for i in range(1 + n // 2) if abun[i] and abun[n - i]))


def euler24():
    """Solution for problem 24."""
    return int(''.join(nth(itertools.permutations(string.digits), 1000000 - 1)))


def euler25(nb_digits=1000):
    """Solution for problem 25."""
    lim = 10 ** (nb_digits - 1)
    for i, f in enumerate(fibo()):
        if f > lim:
            return 1 + i


def length_recur_cycle(a, b, base=10):
    remainders = {}
    for i in itertools.count():
        if a == 0:
            return 0
        if a in remainders:
            return i - remainders[a]
        remainders[a] = i
        a = (a * base) % b


def euler26(lim=1000):
    """Solution for problem 26."""
    return max((length_recur_cycle(1, i), i) for i in range(2, lim))[1]


def euler27(lim=1000):
    """Solution for problem 27."""
    # P(0) = b must be prime
    # P(1) = 1 + a + b must be prime so 1+a+b >= 2 => a => 1-b
    maxa, maxb, maxn = None, None, 0
    for b in primes_up_to(lim):
        for a in range(1 - b, lim + 1):
            assert -lim <= a <= lim
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > maxn:
                maxa, maxb, maxn = a, b, n
    return maxa * maxb


def euler28(n=1001):
    """Solution for problem 28."""
    # For a level of size s (s>1), corners are :
    # s*s, s*s-s+1, s*s-2s+2, s*s-3s+3
    # Their sum is 4*s*s - 6*s + 6  (3 <= s <= n)
    # Writing s = 2*j + 3, sum of corners is
    # 16*j*j + 36j + 24
    # This sum could be computed in constant time but this is
    # fast enough.
    return 1 + sum(16 * j * j + 36 * j + 24 for j in range(n // 2))


def euler29(lima=100, limb=100):
    """Solution for problem 29."""
    n = set()
    for a in range(2, lima + 1):
        p = a
        for _ in range(2, limb + 1):
            p *= a
            n.add(p)
    return len(n)


def euler30():
    """Solution for problem 30."""
    # sum(fifth(digits)) = n
    # nb_digits * fifth(0) < sum(fifth(digits)) <= nb_digits * fifth(base - 1)
    # base ^ (nb_digits - 1) <= n < base ^ nb_digits
    # => base ^ (nb_digits - 1) <= nb_digits * fifth(base - 1)
    # with base = 10, nb_digits <= 6
    fifth = {c: int(c) ** 5 for c in string.digits}
    dict_sum = {}
    for nb_dig in range(2, 6 + 1):
        for l in itertools.combinations_with_replacement('123456789', nb_dig):
            dict_sum.setdefault(sum(fifth[c] for c in l), []).append(list(l))
    return sum(n for n, l in dict_sum.items() if [c for c in sorted(str(n)) if c != '0'] in l)


def euler31(obj=200, coins=[1, 2, 5, 10, 20, 50, 100, 200]):
    """Solution for problem 31."""
    print(obj, coins)
    # TODO


def euler32():
    """Solution for problem 32."""
    # nb_dig(a*b) = nb_dig(a) + nb_dig(b) or nb_dig(a) + nb_dig(b) - 1
    # we want : a * b = c with 0 < a < b < c
    # and we must have : nb_dig(a) + nb_dig(b) + nb_dig(c) = 9
    # i + j + k = 9 and (i + j = k or i + j - 1 = k)
    # => 2i + 2j = 9 (impossible) or 2i + 2j = 10
    # => i + j = 10 => (1, 4, 4), (2, 3, 4).
    return sum({a * b
                for a in range(2, 98)
                for b in range(1234 if a <= 10 else 123, 10000 // a + 1)
                if ''.join(sorted(list(str(a) + str(b) + str(a * b)))) == '123456789'
                })


def euler33():
    """Solution for problem 33."""
    # Different options reducing to b/c (with 0 < b < c < 10 and 0 <= a < 10) are :
    # ab / ac (possible only if a=0 or b=c : not interesting)
    # ba / ca (possible only if a=0 or b=c : not interesting)
    # ab / ca (possible iif 9bc = a (10c - b))
    # ba / ac (possible iif 9bc = a (10b - c))
    # Also, top / bottom = b/c <=> top * c = bottom * b
    t, b = [mult(lst)
            for lst in zip(*[(b, c)
                             for b, c in itertools.combinations(range(1, 10), 2)
                             for a in range(1, 10)
                             for top, bot in [(10 * a + b, 10 * c + a), (10 * b + a, 10 * a + c)]
                             if top * c == bot * b])]
    return b // gcd(t, b)


def euler34():
    """Solution for problem 34."""
    # sum(fact(digits)) = n
    # nb_digits * fact(0) < sum(fact(digits)) <= nb_digits * fact(base - 1)
    # base ^ (nb_digits - 1) <= n < base ^ nb_digits
    # => base ^ (nb_digits - 1) <= nb_digits * fact(base - 1)
    # with base = 10, we have nb_digits <= 7
    fact = {c: math.factorial(int(c)) for c in string.digits}
    dict_sum = {}
    for nb_dig in range(2, 7 + 1):
        for l in itertools.combinations_with_replacement(string.digits, nb_dig):
            dict_sum.setdefault(sum(fact[c] for c in l), []).append(list(l))
    return sum(n for n, l in dict_sum.items() if sorted(str(n)) in l)


def euler35(nb_dig_max=6):
    # permutations of 2 digits or more must contain only 1, 3, 7, 9
    count = 4  # counting 2, 3, 5 and 7
    final_numbers = {'1', '3', '7', '9'}
    for l in range(2, nb_dig_max + 1):
        for p in itertools.product(final_numbers, repeat=l):
            p_int = int(''.join(p))
            perm = {int(''.join(p[i:] + p[:i])) for i in range(len(p))}
            if p_int == min(perm) and all(is_prime(n) for n in perm):
                count += len(perm)
    return count


def euler36():
    """Solution for problem 36."""
    # 999999
    sol = []
    for i in range(1000):
        s = str(i)
        for beg in (-1, -2):
            n = int(s + s[beg::-1])
            s2 = bin(n)[2:]
            if s2 == s2[::-1]:
                sol.append(n)
    return sum(sol)


def euler37():
    """Solution for problem 37."""
    left, sol = {0}, []
    while left:
        left = {n for n in (10 * l + i for i in range(10) for l in left) if is_prime(n)}
        sol.extend(n for n in left if n > 10 and all(is_prime(n % (10 ** pow)) for pow in range(1, len(str(n)))))
    return sum(sol)


def euler38():
    """Solution for problem 38."""
    # '123456789' will be decomposed in at least two elements,
    # the smallest being 4 at most characters long
    sol = 0
    digits = {str(d) for d in range(1, 10)}
    for n in range(10000):
        s = ""
        for i in itertools.count(1):
            s += str(n * i)
            if len(s) >= len(digits):
                if len(s) == len(digits) and set(s) == digits:
                    sol = max(sol, int(s))
                break
    return sol


def euler39(lim=1000):
    """Solution for problem 39."""
    return max((len(list(yield_pythagorean_triples_of_peri(p))), p) for p in range(1, lim + 1))[1]


def euler41():
    """Solution for problem 41."""
    # sum(i, i=1..n) is is not divisible by 3 only if n = 1, 4, 7 or bigger than 9
    for nb_dig in (7, 4, 1):
        for l in itertools.permutations(str(d) for d in range(nb_dig, 0, -1)):
            n = int(''.join(l))
            if is_prime(n):
                return n


def euler43():
    """Solution for problem 43."""
    # Could be optimised by using a constructive solution starting from the end
    div = [(17, 7), (13, 6), (11, 5), (7, 4), (5, 3), (3, 2), (2, 1)]
    return sum(int(''.join(p))
               for p in itertools.permutations(string.digits)
               if all(int(''.join(p[i:i + 3])) % d == 0 for d, i in div))


def euler45(nb_fact=4):
    """Solution for problem 45."""
    t, tn = 0, 0
    p, pn = 0, 0
    h, hn = 0, 0
    while True:
        if p > t:
            t, tn = Tn(tn + 1), tn + 1
        elif t > p or h > p:
            p, pn = Pn(pn + 1), pn + 1
        elif p > h:
            h, hn = Hn(hn + 1), hn + 1
        elif t in [0, 1, 40755]:
            t, tn = Tn(tn + 1), tn + 1
            p, pn = Pn(pn + 1), pn + 1
            h, hn = Hn(hn + 1), hn + 1
        else:
            return t


def euler46():
    """Solution for problem 46."""
    for i in itertools.count(9, 2):
        if not is_prime(i) and not any(is_prime(i - 2 * n * n) for n in range(1, math.ceil(math.sqrt(i // 2)))):
            return i


def euler47(nb_fact=4):
    """Solution for problem 47."""
    cand = []
    for i in itertools.count(2):
        if nb_prime_divisors(i) == nb_fact:
            cand.append(i)
            if len(cand) == nb_fact:
                return cand[0]
        else:
            cand = []


def euler48(n=1000, nb_dig=10):
    """Solution for problem 48."""
    mod = 10 ** nb_dig
    return sum(pow(i, i, mod) for i in range(1, n + 1)) % mod


def sorted_number(n):
    # Reversed to keep 0 instead of` discarding them
    return int(''.join(sorted(str(n), reverse=True)))


def euler49(nb_digit=4):
    """Solution for problem 49."""
    low = 10 ** (nb_digit - 1)
    high = 10 ** nb_digit - 1
    prime = sieve(high)
    prime_perm = {}
    for i in range(low, high + 1):
        if prime[i]:
            prime_perm.setdefault(sorted_number(i), []).append(i)
    for perms in prime_perm.values():
        # could iterate only on a,b but not a bottleneck
        for a, b, c in itertools.combinations(perms, 3):
            assert c > b > a
            if b - a == c - b and a != 1487:
                return int(str(a) + str(b) + str(c))


def euler50(lim=1000000):
    """Solution for problem 50."""
    primes = sieve(lim)
    list_primes = [i for i, p in enumerate(primes) if p]
    max_len, max_sum = 0, 0
    for i in range(len(list_primes)):
        for j in range(i + max_len + 1, len(list_primes)):
            s = sum(list_primes[i:j])  # could use sum array here
            if s > lim:
                break
            elif primes[s]:
                assert j - i > max_len
                max_len, max_sum = j - i, s
    return max_sum


def euler52(lim=6):
    """Solution for problem 52."""
    for x in itertools.count(1):
        digits = sorted_number(x)
        if all(digits == sorted_number(i * x) for i in range(2, lim + 1)):
            return x


def euler57(nb_exp=1000):
    """Solution for problem 57."""
    # If expansion at level n is a/b
    # analysis shows that at level n+1, we have:
    # (2*b+a) / (a+b)
    # Also, gcd(2*b+a, a+b) = gcd(b, a+b) = gcd(a, b)
    # Thus, gcd is conserved : if we start with a reduced
    # fraction, all fractions will be reduced
    nb = 0
    a = b = 1
    for i in range(nb_exp + 1):
        assert gcd(a, b) == 1
        if len(str(a)) > len(str(b)):
            nb += 1
        a, b = 2 * b + a, a + b
    return nb


def euler58(ratio=0.1):
    """Solution for problem 58."""
    # First analysis in euler28
    # Corners are s*s-3s+3, s*s-2s+2, s*s-s+1, s*s
    # s*s is likely not to be prime
    nb_prime = 0
    for s in itertools.count(3, 2):
        for i in range(1, 4):
            if is_prime(s * s - i * s + i):
                nb_prime += 1
        if nb_prime < ratio * (2 * s - 1):
            return s


def euler62(nb_perm=5):
    """Solution for problem 62."""
    cube_perm, l = {}, None
    for i in range(100000):
        c = i * i * i
        new_l = len(str(c))
        if l != new_l:
            cand = [numbers[0]
                    for c, numbers in cube_perm.items() if len(numbers) == nb_perm]
            if cand:
                return min(cand) ** 3
            cube_perm, l = {}, new_l
        cube_perm.setdefault(sorted_number(c), []).append(i)


def euler63():
    """Solution for problem 63."""
    # 10^(n-1) <= x^n < 10^n
    # (n-1) * log(10) <= n * log(x) < n * log(10)
    # (n-1) * log(10) / n <= log(x) < log(10)
    # exp((n-1) * log(10) / n) <= x < 10
    # and LHS becomes bigger than 9 at n = 22
    return sum(
        10 - math.ceil(math.exp((n - 1) * math.log(10) / n))
        for n in range(1, 22))


def euler69(lim=10):
    """Solution for problem 69."""
    return max((i / t, i) for i, t in enumerate(totient(lim)) if i)[1]


def euler70(lim=10000000):
    """Solution for problem 70."""
    n, val = lim, lim
    for i, t in enumerate(totient(lim)):
        if i > 1:
            new_val = i / t
            if new_val < val and sorted_number(i) == sorted_number(t):
                n, val = i, new_val
    return n


def euler87(lim=50000000):
    """Solution for problem 87."""
    # the biggest prime needed p is such that
    # lim >= p**2 + 2**3 + 2**4
    # p <= sqrt(lim - 24)
    primes = list(primes_up_to(int(math.sqrt(lim - 24))))
    sol = set()
    for a in primes:
        sum_a = a ** 4
        if sum_a > lim:
            break
        for b in primes:
            sum_b = sum_a + b ** 3
            if sum_b > lim:
                break
            for c in primes:
                sum_c = sum_b + c ** 2
                if sum_c > lim:
                    break
                sol.add(sum_c)
    return len(sol)


def euler100(lim=1000000000000):
    """Solution for problem 100."""
    # P(BB) = (b/t) * ((b-1)/(t-1))
    # P(BB) = 1/2
    # => 2 * b  * (b - 1) = t * (t - 1)
    # https://oeis.org/A046090
    b0, b1 = 1, 3
    r0, r1 = 0, 1
    while True:
        if b0 + r0 > lim:
            return b0
        b0, b1 = b1, 6 * b1 - b0 - 2
        r0, r1 = r1, 6 * r1 - r0


def euler104(first=True, last=True):
    """Solution for problem 104."""
    digits = sorted('123456789')
    # TODO not efficient enough
    for i, f in enumerate(fibo()):
        s = str(f)
        if (not first or sorted(s[:9]) == digits) \
                and (not last or sorted(s[-9:]) == digits):
            return 1 + i


def increasing_number(n):
    l = str(n)
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def decreasing_number(n):
    l = str(n)
    return all(l[i] >= l[i + 1] for i in range(len(l) - 1))


def bouncy_number(n):
    return not increasing_number(n) and not decreasing_number(n)


def euler112(perc=99):
    """Solution for problem 112."""
    nb_bouncy = 0
    for i in itertools.count(1):
        nb_bouncy += 1 if bouncy_number(i) else 0
        if nb_bouncy * 100 == i * perc:
            return i


def euler124(lim=100000, n=10000):
    """Solution for problem 124."""
    rad = [mult(div) for div in prime_divisors_sieve(lim)]
    rev_rad = {}
    for i, r in enumerate(rad):
        rev_rad.setdefault(r, []).append(i)
    return nth((i for rad in sorted(rev_rad.keys()) for i in rev_rad[rad]), n)


def euler127(lim=120000):
    """Solution for problem 127."""
    # 1) If a, b, c are relatively prime, rad(abc) = rad(a) * rad(b) * rad(c)
    # 2) gcd(a, b) == 1 <=> gcd(rad(a), rad(b)) == 1
    # 3) 1 = gcd(a, c) = gcd(a, c - a) = gcd(a, b) = gcd(a+b, b) = gcd(c, b)
    # 4) As c > rad(abc) > rad(c), we must have rad(c) < c which implies that
    #       2 * rad(c) <= c
    # Technique is the following :
    #  - create a cache simulating the rad function
    #  - create a map from rad values to the (ordered) list of values
    #  - iterate over increasing rad(c) (we can stop early)
    #    - iterate over decreasing c (we can stop early)
    #      - iterate over increasing rad(a) (we can stop early)
    #        - iterate over increasing a (we can stop early)
    #          - check a, compute b, check b
    rad = [mult(div) for div in prime_divisors_sieve(lim - 1)]
    rev_rad = {}
    for i, r in enumerate(rad):
        rev_rad.setdefault(r, []).append(i)
    sorted_rad = sorted(rev_rad.keys())
    s = 0
    for radc in sorted_rad:
        if 2 * radc > lim:
            break
        for c in reversed(rev_rad[radc]):
            if 2 * radc >= c:
                break
            for rada in sorted_rad:
                if 2 * rada * radc >= c:
                    break
                if gcd(rada, radc) == 1:
                    for a in rev_rad[rada]:
                        b = c - a
                        if a >= b:
                            break
                        if b < c and rada * rad[b] * radc < c:
                            s += c
    return s


def euler191(nb_days=4):
    """Solution for problem 191."""
    # 0 late : a, b, c for 0, 1, 2 consecutive absences
    # 1 late : d, e, f for 0, 1, 2 consecutive absences
    a, b, c, d, e, f = 1, 0, 0, 0, 0, 0
    for _ in range(nb_days + 1):  # 1 more iteration to have the res in d
        a, b, c, d, e, f = a + b + c, a, b, a + b + c + d + e + f, d, e
    return d


def euler214(lim=40000000, length=25):
    """Solution for problem 214."""
    tot = totient(lim)
    chains = [0] * (lim + 1)
    for i, t in enumerate(tot):
        chains[i] = 1 + (chains[t] if i > 1 else 0)
    return sum(i for i, (l, t) in enumerate(zip(chains, tot)) if l == length and i == t + 1)


def main():
    """Main function"""
    print("Hello, world!")
    if True:
        assert euler1(10) == 23
        assert euler1() == 233168
        assert euler2() == 4613732
        assert euler3(13195) == 29
        assert euler3() == 6857
        assert euler4(2) == 9009
        assert euler4() == 906609
        assert euler5(10) == 2520
        assert euler5() == 232792560
        assert euler6(10) == 2640
        assert euler6() == 25164150
        assert euler7(6)
        assert euler7() == 104743
        assert euler8(4) == 5832
        assert euler8() == 23514624000
        assert euler9() == 31875000
        assert euler10(10) == 17
        assert euler10() == 142913828922
        assert euler12(5) == 28
        assert euler12() == 76576500
        assert euler15(2, 2) == 6
        assert euler15() == 137846528820
        assert euler16(15) == 26
        assert euler16() == 1366
        assert euler19() == 171
        assert euler20(10) == 27
        assert euler20() == 648
        assert euler21() == 31626
        assert euler22() == 871198282
        assert euler23() == 4179871
        assert euler24() == 2783915460
        assert euler25(3) == 12
        assert euler25() == 4782
        assert euler26(11) == 7
        assert euler26() == 983
        assert euler27() == -59231
        assert euler28(5) == 101
        assert euler28() == 669171001
        assert euler29(5, 5) == 15
        assert euler29() == 9183
        assert euler30() == 443839
        assert euler32() == 45228
        assert euler33() == 100
        assert euler34() == 40730
        assert euler35(2) == 13
        assert euler35() == 55
        assert euler36() == 872187
        assert euler37() == 748317
        assert euler38() == 932718654
        assert euler39() == 840
        assert euler41() == 7652413
        assert euler43() == 16695334890
        assert euler45() == 1533776805
        assert euler46() == 5777
        assert euler47(2) == 14
        assert euler47(3) == 644
        assert euler47()
        assert euler48(10, 10) == 405071317
        assert euler48() == 9110846700
        assert euler49(1) is None
        assert euler49(2) is None
        assert euler49(3) is None
        assert euler49() == 296962999629
        assert euler50(100) == 41
        assert euler50(1000) == 953
        assert euler50() == 997651
        assert euler52(2) == 125874
        assert euler52() == 142857
        assert euler57(10) == 1
        assert euler57() == 153
        assert euler58() == 26241
        assert euler62(3) == 41063625
        assert euler62() == 127035954683
        assert euler63() == 49
        assert euler69(10) == 6
        assert euler69(1000000) == 510510
        assert euler70() == 8319823
        assert euler87(50) == 4
        assert euler87(50000000) == 1097343
        assert euler100() == 756872327473
        assert euler104(False, False) == 1
        assert euler104(False, True) == 541
        assert euler104(True, False) == 2749
        # TOO SLOW : euler104(True, True)
        assert euler112(90) == 21780
        # TOO SLOW : print(euler112())
        assert euler124(10, 4) == 8
        assert euler124(10, 6) == 9
        assert euler124() == 21417
        assert euler127(1000) == 12523
        assert euler127() == 18407904
        assert euler191(4) == 43
        assert euler191(30) == 1918080160
        assert euler214(20, 4) == 12
        assert euler214(40000000, 25) == 1677366278943

if __name__ == "__main__":
    main()
