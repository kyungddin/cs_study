#include <iostream>
#include <thread>

using namespace std;

bool m_run = 0;
int num = 0;
thread m_thread;

void start();
void stop();
void run();

void start()
{
	m_run = 1;
	m_thread = thread(run);
}

//m_thread.~thread()
//m_thread = new thread(run)
//객체를 재할당 시 소멸자가 발동!!

void stop()
{
	m_run = 0;
}

void run()
{
	while (m_run == 1)
	{
		num++;
	}
}

// worker thread 종료되어도.. thread 객체는 정리가 필요하다 joinable`하다고..
// 마치 zombie process같은 상태.. 즉 os의 추가적인 정리인 join이 필요하다

int main()
{
	start();
	stop();
	start();
}