from tictactoe import player, EMPTY, X, O, actions, result, winner, terminal, utility


# print(
#     player(
#         [
#             [O, EMPTY, X],
#             [EMPTY, O, O],
#             [X, X, X],
#         ]
#     )
# )

# print(
#     actions(
#         [
#             [O, EMPTY, X],
#             [EMPTY, O, O],
#             [X, EMPTY, X],
#         ]
#     )
# )

# print(
#     result(
#         [
#             [O, EMPTY, X],
#             [EMPTY, O, O],
#             [X, EMPTY, X],
#         ],
#         (2, 1),
#     )
# )

# print(
#     winner(
#         [
#             [EMPTY, O, O],
#             [X, O, X],
#             [X, O, X],
#         ]
#     )
# )

# print(
#     terminal(
#         [
#             [O, X, O],
#             [X, O, O],
#             [X, X, X],
#         ]
#     )
# )

print(
    utility(
        [
            [X, O, X],
            [O, O, X],
            [X, X, O],
        ]
    )
)
