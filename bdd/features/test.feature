Feature: Test Feature

Scenario Outline: Verificar se faz a listagem de alunos
Given seleciono a massa "test"
When executo um "POST" com a informação do cenario <cenario>
Then o sistema me traz a listagem de alunos
Examples:
    | cenario |
    | CENARIO |  