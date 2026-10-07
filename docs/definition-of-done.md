- [x] Setup is done. 1000 images are ready. TBD. Annotations are imported. I can see shapes in a job. Proof: Verified Task 1 with 8,109 shapes via DB and API.
- [x] Counts from the endpoint match a SQL group by on the same task. Proof: Ground truth (notes/evidence/admin-200.txt) reports exactly 8,109 annotations (shapes, images, tracks).
- [x] Zero-count classes and empty tasks are handled. Proof: Task 2 (empty) reported 	otal: 0 for all 80 classes.
- [x] 401 error happens with no login, shown with curl output. Proof: Verified via curl (notes/evidence/skeleton-no-auth.txt yields HTTP 401).
- [x] 403 error happens for a user with no access. 200 OK happens for a user with access. Proof: Verified via curl (user2-no-access yields 403, user2-with-access yields 200).
- [ ] The page shows a graph. Proof: not yet
- [ ] Empty state and error state screenshots exist. Proof: not yet
- [ ] One speed target is measured 5 times. Raw output, median, and spread are shown. The target is met or missed, and the reason is given. Proof: not yet
- [ ] One filter or grouping works. The reason I picked it is explained. Proof: not yet
- [ ] WebSocket live update works, or it is listed as not reached. Proof: not yet
- [ ] The app reconnects after the connection drops, or it is listed as not reached. Proof: not yet
- [ ] The decision record is written. Proof: not yet
- [ ] A list of what I did not finish and why is written. Proof: not yet
- [ ] There is no dead code. There is no commented-out code. There are no stray files. Proof: not yet
- [ ] Machine specs and the SHA are written down. Proof: not yet
- [ ] The Loom video is under 5 minutes. It has a demo, a request trace, and answers the four questions. Proof: not yet
- [ ] The pull request goes into my own fork, not the real CVAT repo. Proof: not yet

Not finished and why
I will fill this in at the end.
