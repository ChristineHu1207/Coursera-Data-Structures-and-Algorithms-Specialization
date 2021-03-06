#include <algorithm>
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <cstdio>
#include <map>

using std::make_pair;
using std::map;
using std::pair;
using std::string;
using std::vector;
using std::stack;
using std::cin;
using std::cout;
using std::endl;

struct suffix_tree_node {
    suffix_tree_node* parent{ nullptr };
    map<char, suffix_tree_node*> children;
    int string_depth{ 0 };
    int edge_start{ -1 };
    int edge_end{ -1 };
};

suffix_tree_node snodes_buf[400000];
int cur_buf_index = 0;

inline suffix_tree_node* new_tree_node(suffix_tree_node* parent, int depth, int start, int end)
{
    snodes_buf[cur_buf_index].parent = parent;
    snodes_buf[cur_buf_index].string_depth = depth;
    snodes_buf[cur_buf_index].edge_start = start;
    snodes_buf[cur_buf_index].edge_end = end;

    return &(snodes_buf[cur_buf_index++]);
}

inline suffix_tree_node* create_new_leaf(suffix_tree_node* node, const string& S, int suffix)
{
    suffix_tree_node* leaf = new_tree_node(node, S.size() - suffix, suffix + node->string_depth, S.size() - 1);
    node->children[S[leaf->edge_start]] = leaf;

    return leaf;
}

inline suffix_tree_node* breake_edge(suffix_tree_node* node, const string& S, int start, int offset)
{
    char startChar = S[start];
    char midChar = S[start + offset];

    suffix_tree_node* midNode = new_tree_node(node, node->string_depth + offset, start, start + offset - 1);
    midNode->children[midChar] = node->children[startChar];
    node->children[startChar]->parent = midNode;
    node->children[startChar]->edge_start += offset;
    node->children[startChar] = midNode;

    return midNode;
}

suffix_tree_node* suffix_tree_from_array(const string& S, const vector<int>& order, const vector<int>& lcp_array)
{
    suffix_tree_node* root = new_tree_node(nullptr, 0, -1, -1);
    suffix_tree_node* curNode = root;

    int lcpPrev = 0;
    const int N = S.size();

    for (int i = 0; i < N; ++i) {
        auto suffix = order[i];

        while (curNode->string_depth > lcpPrev) {
            curNode = curNode->parent;
        }

        if (curNode->string_depth == lcpPrev) {
            curNode = create_new_leaf(curNode, S, suffix);
        }
        else {
            int edge_start = order[i - 1] + curNode->string_depth;
            int offset = lcpPrev - curNode->string_depth;
            suffix_tree_node* midNode = breake_edge(curNode, S, edge_start, offset);
            curNode = create_new_leaf(midNode, S, suffix);
        }

        if (i < N - 1) {
            lcpPrev = lcp_array[i];
        }
    }

    return root;
}

void recursive_preorder_print(suffix_tree_node* node)
{
    cout << node->edge_start << ' ' << node->edge_end + 1 << '\n';

    for (auto& next : node->children) {
        recursive_preorder_print(next.second);
    }
}

void iterative_preorder_print(suffix_tree_node* root)
{
    stack<suffix_tree_node*> nodeStack;

    for (auto iter = root->children.rbegin(); iter != root->children.rend(); ++iter) {
        nodeStack.push(iter->second);
    }

    while (!nodeStack.empty()) {

        suffix_tree_node* node = nodeStack.top();
        nodeStack.pop();

        cout << node->edge_start << ' ' << node->edge_end + 1 << '\n';

        for (auto iter = node->children.rbegin(); iter != node->children.rend(); ++iter) {
            nodeStack.push(iter->second);
        }
    }
}

int main()
{
    std::ios::sync_with_stdio(false);

    string text;
    cin >> text;

    vector<int> suffix_array(text.size());
    vector<int> lcp_array(text.size() - 1);

    for (int j = 0, N = text.size(); j < N; ++j) {
        cin >> suffix_array[j];
    }

    for (int j = 0, N = text.size() - 1; j < N; ++j) {
        cin >> lcp_array[j];
    }

    suffix_tree_node* root = suffix_tree_from_array(text, suffix_array, lcp_array);

    cout << text << endl;

    iterative_preorder_print(root);

    return 0;
}