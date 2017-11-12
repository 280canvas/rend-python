import json
import io

from antlr4 import *

from ANTLR.twoeightyLexer import twoeightyLexer
from ANTLR.twoeightyListener import twoeightyListener
from ANTLR.twoeightyParser import twoeightyParser


class astBuilder(twoeightyListener):
    def __init__(self):
        self.root = {
            "variables": {},
            "loop": 0,
            "statements": []
        }

    def enterProgram(self, ctx:twoeightyParser.ProgramContext):
        pass

    # Exit a parse tree produced by twoeightyParser#program.
    def exitProgram(self, ctx:twoeightyParser.ProgramContext):
        pass


    # Enter a parse tree produced by twoeightyParser#variableDec.
    def enterVariableDec(self, ctx:twoeightyParser.VariableDecContext):
        self.root["variables"][ctx.ID().getText()] = self.valueExp(ctx.value())

    # Exit a parse tree produced by twoeightyParser#variableDec.
    def exitVariableDec(self, ctx:twoeightyParser.VariableDecContext):
        pass


    # Enter a parse tree produced by twoeightyParser#loop.
    def enterLoop(self, ctx:twoeightyParser.LoopContext):
        length = int(ctx.INT().getText())
        if ctx.unit.text == 's':
            length = length*1000
        self.root["loop"] = length

    # Exit a parse tree produced by twoeightyParser#loop.
    def exitLoop(self, ctx:twoeightyParser.LoopContext):
        pass


    # Enter a parse tree produced by twoeightyParser#statement.
    def enterStatement(self, ctx:twoeightyParser.StatementContext):
        pass

    # Exit a parse tree produced by twoeightyParser#statement.
    def exitStatement(self, ctx:twoeightyParser.StatementContext):
        pass


    # Enter a parse tree produced by twoeightyParser#clear.
    def enterClear(self, ctx:twoeightyParser.ClearContext):
        self.root["statements"].append({"instruction": "clear"})

    # Exit a parse tree produced by twoeightyParser#clear.
    def exitClear(self, ctx:twoeightyParser.ClearContext):
        pass


    # Enter a parse tree produced by twoeightyParser#colour.
    def enterColour(self, ctx:twoeightyParser.ColourContext):
        self.root["statements"].append({"instruction": "colour",
                                        "colour": ctx.COLOUR().getText()
                                        })

    # Exit a parse tree produced by twoeightyParser#colour.
    def exitColour(self, ctx:twoeightyParser.ColourContext):
        pass


    # Enter a parse tree produced by twoeightyParser#shape.
    def enterShape(self, ctx:twoeightyParser.ShapeContext):
        pass

    # Exit a parse tree produced by twoeightyParser#shape.
    def exitShape(self, ctx:twoeightyParser.ShapeContext):
        pass


    # Enter a parse tree produced by twoeightyParser#rectangle.
    def enterRectangle(self, ctx:twoeightyParser.RectangleContext):
        self.root["statements"].append({"instruction": "rectangle",
                                        "x": self.valueExp(ctx.x),
                                        "y": self.valueExp(ctx.y),
                                        "w": self.valueExp(ctx.w),
                                        "h": self.valueExp(ctx.h)})

    # Exit a parse tree produced by twoeightyParser#rectangle.
    def exitRectangle(self, ctx:twoeightyParser.RectangleContext):
        pass


    # Enter a parse tree produced by twoeightyParser#circle.
    def enterCircle(self, ctx:twoeightyParser.CircleContext):
        self.root["statements"].append({"instruction": "circle",
                                        "x": self.valueExp(ctx.x),
                                        "y": self.valueExp(ctx.y),
                                        "r": self.valueExp(ctx.r)})

    # Exit a parse tree produced by twoeightyParser#circle.
    def exitCircle(self, ctx:twoeightyParser.CircleContext):
        pass


    # Enter a parse tree produced by twoeightyParser#line.
    def enterLine(self, ctx:twoeightyParser.LineContext):
        self.root["statements"].append({"instruction": "line",
                                        "x1": self.valueExp(ctx.x1),
                                        "y1": self.valueExp(ctx.y1),
                                        "x2": self.valueExp(ctx.x2),
                                        "y2": self.valueExp(ctx.y2)})

    # Exit a parse tree produced by twoeightyParser#line.
    def exitLine(self, ctx:twoeightyParser.LineContext):
        pass


    # Enter a parse tree produced by twoeightyParser#arc.
    def enterArc(self, ctx:twoeightyParser.ArcContext):
        self.root["statements"].append({"instruction": "arc",
                                        "x1": self.valueExp(ctx.x1),
                                        "y1": self.valueExp(ctx.y1),
                                        "x2": self.valueExp(ctx.x2),
                                        "y2": self.valueExp(ctx.y2),
                                        "cx": self.valueExp(ctx.cx),
                                        "cy": self.valueExp(ctx.cy)})

    # Exit a parse tree produced by twoeightyParser#arc.
    def exitArc(self, ctx:twoeightyParser.ArcContext):
        pass
    
    
    # Enter a parse tree produced by twoeightyParser#increment.
    def enterIncrement(self, ctx:twoeightyParser.IncrementContext):
        id = ctx.ID().getText()
        return self.root["statements"].append({"instruction": "assign",
                                                "identifier": id,
                                                'value': {'returns': 'binop',
                                                          'binop': {
                                                              'l': {'returns': 'variable', 'variable': 'x'},
                                                              'r': {'returns': 'integer', 'integer': 1},
                                                              'op': '+'
                                                              }
                                                        }
                                                })

    # Exit a parse tree produced by twoeightyParser#increment.
    def exitIncrement(self, ctx:twoeightyParser.IncrementContext):
        pass


    # Enter a parse tree produced by twoeightyParser#decrement.
    def enterDecrement(self, ctx:twoeightyParser.DecrementContext):
        return self.root["statements"].append({"instruction": "assign",
                                                "identifier": id,
                                                'value': {'returns': 'binop',
                                                          'binop': {
                                                              'l': {'returns': 'variable', 'variable': 'x'},
                                                              'r': {'returns': 'integer', 'integer': 1},
                                                              'op': '-'
                                                              }
                                                        }
                                                })

    # Exit a parse tree produced by twoeightyParser#decrement.
    def exitDecrement(self, ctx:twoeightyParser.DecrementContext):
        pass


    # Enter a parse tree produced by twoeightyParser#variableAssign.
    def enterVariableAssign(self, ctx:twoeightyParser.VariableAssignContext):
        self.root["statements"].append({"instruction": "assign",
                                        "identifier": ctx.ID().getText(),
                                        "value": self.valueExp(ctx.value())
                                        })

    # Exit a parse tree produced by twoeightyParser#variableAssign.
    def exitVariableAssign(self, ctx:twoeightyParser.VariableAssignContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Integer.
    def enterInteger(self, ctx:twoeightyParser.IntegerContext):
        return int(ctx.getText())

    # Exit a parse tree produced by twoeightyParser#Integer.
    def exitInteger(self, ctx:twoeightyParser.IntegerContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Variable.
    def enterVariable(self, ctx:twoeightyParser.VariableContext):
        return ctx.getText()

    # Exit a parse tree produced by twoeightyParser#Variable.
    def exitVariable(self, ctx:twoeightyParser.VariableContext):
        pass


    # Enter a parse tree produced by twoeightyParser#Thousand.
    def enterThousand(self, ctx:twoeightyParser.ThousandContext):
        pass

    # Exit a parse tree produced by twoeightyParser#Thousand.
    def exitThousand(self, ctx:twoeightyParser.ThousandContext):
        pass


    # Enter a parse tree produced by twoeightyParser#MathFunc.
    def enterMathFunc(self, ctx:twoeightyParser.MathFuncContext):
        func = ctx.funccall().getText()
        args = [self.valueExp(x) for x in ctx.value()]
        if func == 'rand':
            func = 'random'
        return {"functionName": func,
                "arguments": args}

    # Exit a parse tree produced by twoeightyParser#MathFunc.
    def exitMathFunc(self, ctx:twoeightyParser.MathFuncContext):
        pass

    # Enter a parse tree produced by twoeightyParser#Binop.
    def enterBinop(self, ctx:twoeightyParser.BinopContext):
        return {"l": self.valueExp(ctx.l),
                "r": self.valueExp(ctx.r),
                "op": ctx.op().getText()
                }

    # Exit a parse tree produced by twoeightyParser#Binop.
    def exitBinop(self, ctx:twoeightyParser.BinopContext):
        pass


    # Enter a parse tree produced by twoeightyParser#op.
    def enterOp(self, ctx:twoeightyParser.OpContext):
        pass

    # Exit a parse tree produced by twoeightyParser#op.
    def exitOp(self, ctx:twoeightyParser.OpContext):
        pass

    # Enter a parse tree produced by twoeightyParser#funccall.
    def enterFunccall(self, ctx:twoeightyParser.FunccallContext):
        pass


    # Exit a parse tree produced by twoeightyParser#funccall.
    def exitFunccall(self, ctx:twoeightyParser.FunccallContext):
        pass
    
    def valueExp(self, ctx:twoeightyParser.ValueContext):
        t = type(ctx)
        returnType = ""
        result = None
        if t is twoeightyParser.IntegerContext:
            returnType = "integer"
            result = self.enterInteger(ctx)
        elif t is twoeightyParser.ThousandContext:
            returnType = "integer"
            result = 1000
        elif t is twoeightyParser.VariableContext:
            returnType = "variable"
            result = self.enterVariable(ctx)
        elif t is twoeightyParser.BinopContext:
            returnType = "binop"
            result = self.enterBinop(ctx)
        elif t is twoeightyParser.MathFuncContext:
            returnType = "funccall"
            result = self.enterMathFunc(ctx)
        else:
            raise Exception(t, returnType, ctx)
        return {"returns": returnType,
                returnType: result}

def parse(tweet):
    tweetStream = InputStream(tweet)
    lexer = twoeightyLexer(tweetStream)
    stream = CommonTokenStream(lexer)
    parser = twoeightyParser(stream)
    tree = parser.program()
    builder = astBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)
    encoder = json.JSONEncoder()

    return encoder.encode(builder.root)


print(parse("x=0;500 ms:clr;c 500,500,100*sin(x);x++;"))
