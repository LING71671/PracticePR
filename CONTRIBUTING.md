# 贡献指南

## 先确认任务

选择一个未完成的 Issue，确认没有正在处理的 PR，留言说明准备怎样修改，等待维护者确认。

“添加自己的练习记录”是每个人都可以参与的任务：使用 Issue 中的“练习任务”模板，创建标题为 `添加练习记录：你的用户名` 的独立 Issue，列出你的文件路径和验收条件。它只对应你自己的 PR。

修改前先阅读对应 Issue 的验收条件。翻译任务应保留原意，文档任务应检查链接和操作步骤。发现任务范围需要调整时，先在 Issue 中讨论。

## 方式一：只用浏览器

1. 在本仓库右上角点击 **Fork**，在自己的账号下创建副本。
2. 在自己的 Fork 中打开分支选择器，输入分支名，例如 `docs/add-your-name`，从 `main` 创建分支，并确认当前选中它。
3. 打开需要修改的文件，点击编辑；新文件可以使用 **Add file → Create new file**。新增练习记录时，将 [模板](templates/participant.md) 的内容复制到 `participants/你的GitHub用户名.md`，替换示例用户名和说明。
4. 点击 **Commit changes**，填写具体的提交说明，例如 `docs: add practice record for octocat`，将提交保存到刚才的任务分支。
5. 返回 Fork 首页，点击 **Contribute → Open pull request**。如果按钮没有出现，在原仓库的 **Pull requests → New pull request → compare across forks** 中选择自己的 Fork 和任务分支。
6. 检查目标仓库为 `LING71671/PracticePR`，目标分支为 `main`，来源为你的 Fork 和任务分支。
7. 阅读 **Files changed**，确认只包含本次任务的修改。按 PR 模板填写描述，把 `Closes #` 后面补上你要完成的 Issue 编号，再提交。

不完整的内容可以先提交 **Draft pull request**；准备好接受审阅后，再点击 **Ready for review**。

## 方式二：在本地使用 Git

先在 GitHub 网页完成 Fork，并安装 Git。下列命令中的 `YOUR_USERNAME` 都需要替换成你自己的 GitHub 用户名。

```sh
git clone https://github.com/YOUR_USERNAME/PracticePR.git
cd PracticePR
git remote add upstream https://github.com/LING71671/PracticePR.git
git switch -c docs/add-YOUR_USERNAME
```

用编辑器完成任务。新增练习记录时，复制 `templates/participant.md`，保存为 `participants/YOUR_USERNAME.md`，替换模板内容。

```sh
git status
git diff
python scripts/check_participants.py
git add participants/YOUR_USERNAME.md
git commit -m "docs: add practice record for YOUR_USERNAME"
git push -u origin docs/add-YOUR_USERNAME
```

`git add` 后面填写本次实际修改的文件；翻译任务的路径会与上例不同。Python 检查需要 Python 3.10 或更高版本；不安装 Python 也能用网页完成练习，PR 中会执行相同检查。

推送后，按“方式一”的第 5–7 步创建 PR。

## 提交 PR 前

- 一条 PR 对应一项任务，标题清楚说明修改内容。
- 提交说明使用 `docs:`、`fix:`、`feat:` 或 `chore:` 等前缀，例如 `docs: translate README into English`。
- 阅读完整差异，确认没有无关文件、私人信息或误删内容。
- 按 Issue 的验收条件检查结果，在 PR 中写明你实际做过的检查。
- 在描述中使用 `Closes #123` 关联本仓库中对应的具体任务，实际填写时替换编号。长期开放的任务入口使用 `Refs #123`，避免把公共入口关闭。
- 自己新增的链接应能打开，Markdown 应在 GitHub 预览中正常显示。

## 自动检查与人工审阅

每条 PR 都会运行 `validate` 检查，验证 `participants/` 下的记录格式。文档任务仍需根据验收条件自行检查内容。

首次从 Fork 提交时，GitHub 可能要求维护者批准工作流运行；看到等待批准时，无需重新提交 PR。

检查失败时，打开 **Checks → validate**，查看错误。修正后提交到同一个分支，检查会重新运行。

维护者会亲自审阅 PR。审阅可能提出问题、要求修改或批准。请回复具体意见，在原分支上继续提交；不需要为同一个任务重新创建 PR。修改后说明调整了哪些内容，方便复审。

批准和检查通过后，由维护者手动合并。读者不需要合并权限。

## 合并之后

目标为默认分支 `main` 的 PR 合并后，描述中以 `Closes #编号` 关联的 Issue 会自动关闭。确认自己的文件或修改已出现在原仓库，再清理任务分支。

网页操作：回到自己的 Fork，在 `main` 分支使用 **Sync fork → Update branch**。合并后的任务分支可以通过 PR 页面上的 **Delete branch** 删除。

本地操作：先确认工作区没有未提交的修改，再同步。

```sh
git switch main
git fetch upstream
git merge --ff-only upstream/main
git push origin main
```

然后删除本地任务分支和远端任务分支。将分支名替换成你实际使用的名称：

```sh
git branch -d docs/add-YOUR_USERNAME
git push origin --delete docs/add-YOUR_USERNAME
```

如果 PR 使用 Squash 合并，`git branch -d` 可能提示未合并。先保留分支，确认 PR 状态、原仓库里的最终内容及本地分支没有遗漏修改后，再决定是否使用 `-D` 删除。

同步遇到分支分叉或冲突时，先保留现场，在自己的 PR 中说明情况。不要通过强制推送覆盖不清楚的修改。

## 给维护者

1. 确认 Issue 的任务范围和验收条件，协调重复认领。
2. 检查 PR 的目标分支、完整差异和关联 Issue；批准外部工作流前，查看是否改动了工作流或脚本。
3. 检查内容准确性和链接，结合自动检查结果给出明确的审阅意见。
4. 需要修改时使用 **Request changes**，复审通过后使用 **Approve**。提出修改的原因，给读者留下继续提交的机会。
5. 手动使用 **Squash and merge** 合并，在提交标题中保留合适的 Conventional Commits 前缀，并确认对应任务关闭。

## 官方操作说明

- [从 Fork 创建 PR](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)
- [关联 PR 与 Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
