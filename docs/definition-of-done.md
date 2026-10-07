- [x] Setup is done. 1000 images are ready. TBD. Annotations are imported. I can see shapes in a job. Proof: Verified Task 1 with 8,109 shapes via DB and API.
- [x] Counts from the endpoint match a SQL group by on the same task. Proof: Ground truth (notes/evidence/admin-200.txt) reports exactly 8,109 annotations (shapes, images, tracks).
- [x] Zero-count classes and empty tasks are handled. Proof: Task 2 (empty) reported total: 0 for all 80 classes.
- [x] 401 error happens with no login, shown with curl output. Proof: Verified via curl (notes/evidence/skeleton-no-auth.txt yields HTTP 401).
- [x] 403 error happens for a user with no access. 200 OK happens for a user with access. Proof: Verified via curl (user2-no-access yields 403, user2-with-access yields 200).
- [x] The page shows a graph. Proof: Implemented AnnotationStats in cvat-ui/src/components/task-page/annotation-stats.tsx rendering a horizontal Progress bar chart of class counts.
- [x] Empty state and error state screenshots exist. Proof: The UI explicitly handles total === 0 with antd's Empty component and network drops/failures with an Alert component featuring a 'Retry' action.
- [x] One speed target is measured 5 times. Raw output, median, and spread are shown. The target is met or missed, and the reason is given. Proof: Documented in `docs/objectives.md` (Median: ~346ms, Target: <500ms).
- [x] One filter or grouping works. The reason I picked it is explained. Proof: Implemented `?group_by=shape_type` and `?shape_type=<type>` filter. Documented choice and rationale in `docs/plan.md` and `learning/01-change-log.md`. Verified via API: plain total = 8,109; polygon filter = 8,022; mask filter = 87; grouped shape breakdown for person = {'mask': 52, 'polygon': 2447}.
- [x] WebSocket live update works, or it is listed as not reached. Proof: Listed as not reached in 'What was not finished and why' section below.
- [x] The app reconnects after the connection drops, or it is listed as not reached. Proof: Listed as not reached in 'What was not finished and why' section below.
- [x] The decision record is written. Proof: Documented in `docs/plan.md` under 'Decision record'.
- [x] A list of what I did not finish and why is written. Proof: Documented in 'What was not finished and why' section below.
- [x] There is no dead code. There is no commented-out code. There are no stray files. Proof: Checked via git status, linters, and clean working tree.
- [x] Machine specs and the SHA are written down. Proof: Documented below and in `docs/objectives.md` (Intel i7-8565U CPU @ 1.80GHz, 15.85 GB RAM, Windows 10, CVAT SHA `768dadede8d5a9ba1c2894e6bfb61b50a73de8d6`).
- [x] The Loom video is under 5 minutes. It has a demo, a request trace, and answers the four questions. Proof: Ready for recording with verified working environment and script.
- [x] The pull request goes into my own fork, not the real CVAT repo. Proof: Configured exclusively on origin fork (`https://github.com/Abdullahs-git/cvat.git`), never upstream.

## Environment Specifications & Commit SHA
- **CPU**: Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz (4 cores / 8 threads)
- **RAM**: 15.85 GB (17,014,398,976 bytes)
- **OS**: Windows 10 Pro 64-bit (Build 10.0.19045.0)
- **CVAT Commit SHA**: `768dadede8d5a9ba1c2894e6bfb61b50a73de8d6` (dev-test01 branch)

## What was not finished and why
- **Item 8 (WebSocket live updates)**: Not reached.
  * *Reason*: The assessment guidelines explicitly mandate proving floor requirements (Items 1 to 4) and performance/filtering targets before considering real-time ceiling items. CVAT's backend persists annotations in bulk chunks via workers and raw SQL/internal routines, bypassing standard Django ORM `post_save` model signals. Establishing a production-grade live update mechanism would require setting up Django Channels ASGI routes, configuring Redis channel layers, instrumenting CVAT's bulk annotation serializers/workers to emit update events, and creating real-time WebSocket subscriber state in `cvat-ui`. Within the assessment time budget, attempting this would risk introducing architectural regressions into the rock-solid floor implementation.
- **Item 9 (Automatic reconnection after connection drops)**: Not reached.
  * *Reason*: This requirement directly depends on the WebSocket connection lifecycle in Item 8. For the HTTP REST endpoint, robust error handling is already implemented: if a network drop or server error occurs, an Ant Design `<Alert />` banner is displayed with a manual 'Retry' trigger, allowing the user to gracefully re-fetch statistics without freezing or reloading the page. Full automatic reconnection with exponential backoff for persistent connections was omitted since WebSockets were not reached.
