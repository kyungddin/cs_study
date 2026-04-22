# MFC
MFC 플젝 하면서 공부한 거 기록하기


## View
- MFC에서는 프레임워크가 자동으로 View를 띄워주므로, MainFrm에서 굳이 객체를 안
만들어도 자동으로 생성됨

- 그러나, 이러한 작업은 실제로는 프로젝트.cpp 소스에서 이루어짐
    - `RUNTIME_CLASS(); ` 메서드가 해당 클래스를 만들어서 매핑해준다


## CView vs CDialog
- CView
    - 부모 프레임(Client Area)에 붙음
    - 프레임 크기 변화에 따라 같이 Resize됨 (조건 있음)
        - OnSize()를 통해 크기 변경 이벤트 처리를 해줘야 함
        - 처리 방식에 대해서는 코드 참고해보기
- CDialog
    - 기본적으로 고정 좌표 기반 UI
    - 자동 Resize 없음 (직접 처리해야 함)


## OnSize() 테크닉
- `void CMyView::OnSize(UINT nType, int cx, int cy);`
    - 윈도우 크기가 바뀌었다고 MFC가 알려주는 이벤트 함수
    - 그냥 알림 이상도 이하도 아님

- `MoveWindow(x, y, width=cx, height=cy);`
    - (x,y) 좌표를 기준으로 cx와 cy만큼 변환
    - 좌표는 해당 부모(View, Frame 등)이 기준이 된다


## CView vs CFormView
- CFormView는 기존의 CView에서 리소스 UI 사용이 가능한 View
- 단점
    ```markdown
    1) 자유도가 낮음
    - 그래픽 UI 만들기 어려움
    - 커스텀 렌더링 한계

    2) MFC “View 철학” 일부 포기
    - CView처럼 OnDraw 기반 구조 아님

    3) 복잡한 UI에서 한계
    - Visual Studio 같은 UI 만들 땐 부족
    ```


## DockingView vs SplitView
둘 다 SDI에서 단일 View를 여러 창으로 구성하고 싶을 때 사용하는 테크닉이다

1. Docking View
- Purpose: 사용자가 UI 커스터마이징, 창 숨김/이동 필요, 복잡하지만 유연함이 필요할 때
    - View는 그대로 둠 (중앙)
    - Docking은 Frame이 담당
    - Pane이 “창” 역할

- 사용방법:
    - 1. Pane 생성 (클래스 마법사 사용하기)
    ```cpp
    class CLeftPane : public CDockablePane
    {
    public:
        CTreeCtrl m_tree;
    };
    ```

    - 2. MainFrame에 멤버 추가
    ```cpp
    class CMainFrame : public CFrameWndEx
    {
        CLeftPane m_wndLeftPane;
    };
    ```

    - 3. OnCreate에서 생성
    ```cpp
    int CMainFrame::OnCreate(LPCREATESTRUCT lpCreateStruct)
    {
        CFrameWndEx::OnCreate(lpCreateStruct);

        EnableDocking(CBRS_ALIGN_ANY);

        m_wndLeftPane.Create(
            _T("Left Pane"),
            this,
            CRect(0, 0, 200, 300),
            TRUE,
            ID_VIEW_LEFT,
            WS_CHILD | WS_VISIBLE | CBRS_LEFT);

        m_wndLeftPane.EnableDocking(CBRS_ALIGN_LEFT);

        DockPane(&m_wndLeftPane);

        return 0;
    }
    ```

    - 4. Pane 안에 컨트롤 넣기
    ```cpp
    int CLeftPane::OnCreate(LPCREATESTRUCT lpCreateStruct)
    {
        CDockablePane::OnCreate(lpCreateStruct);

        m_tree.Create(
            WS_CHILD | WS_VISIBLE | TVS_HASLINES,
            CRect(0, 0, 200, 300),
            this,
            1);

        return 0;
    }
    ```


2. Split View
- Purpose: 하나의 Frame(Client Area)을 여러 View 영역으로 나누는 구조
    - 사용자가 “창처럼 분리/도킹” 못 함
    - 대신 “항상 일정한 구조”

- 구현 방법
    - 1. View 클래스 준비
        - Spliteer는 View를 칸으로 나누는 구조라서 View부터
        있어야 한다네요
    ```cpp
    class CLeftView : public CView
    {
    };

    class CRightView : public CView
    {
    };    
    ```

    - 2. MainFrame에 Splitter 멤버 추가
    ```cpp
    class CMainFrame : public CFrameWndEx
    {
    protected:
        CSplitterWnd m_wndSplitter;
    };
    ```

    - 3. OnCreateClient에서 Splitter 생성 (핵심)
        - Docking은 OnCreate에서 생성했었다..
    ```cpp
    BOOL CMainFrame::OnCreateClient(LPCREATESTRUCT lpcs, CCreateContext* pContext)
    {
        return m_wndSplitter.CreateStatic(this, 1, 2) &&  // 1행 2열
            m_wndSplitter.CreateView(0, 0, RUNTIME_CLASS(CLeftView),
                                        CSize(200, 0), pContext) &&
            m_wndSplitter.CreateView(0, 1, RUNTIME_CLASS(CRightView),
                                        CSize(0, 0), pContext);
    }
    ```

    - 정리하자면.. MainFrm의 wndSplitter 멤버 변수의 각 위치에 View를 할당하는 구조


## 컨트롤 변수
- 리소스(도구)를 조작하기 위한 변수
- 해당 리소스를 리소스 뷰에서 우클릭 후 변수를 추가하며, 범주는 Control이어야 한다
- 반드시 초기화 함수가 따라와줘야 한다
    - 클래스 마법사에서 OnInitialUpdate를 찾아 추가해준다 (가상 함수임)


## List Control
- 우리가 흔히 보는 표 형태의 도구
- 표 형태로 보려면 속성에서 보기를 반드시 Report로 설정해줘야 한다
- 컨트롤 변수를 생성하고 가상 함수로 초기화해주기~
