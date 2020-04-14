#include <iostream>
#include <chrono>
#include <date/date.h>

int main()
{
    using namespace std::chrono;
    using namespace date;

    auto tp = system_clock::now();
    std::cout << tp << '\n';
}
