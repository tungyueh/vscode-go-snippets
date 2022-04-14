import pytest

from main import replace_textmate_syntax

test_case = {
  "single import": {
    "actual": "import \"${1:package}\"",
    "expect": "import \"package\""
  },
  "multiple imports": {
    "actual": "import (\n\t\"${1:package}\"\n)",
    "expect": "import (\n\t\"package\"\n)"
  },
  "single constant": {
    "actual": "const ${1:name} = ${2:value}",
    "expect": "const name = value"
  },
  "multiple constants": {
    "actual": "const (\n\t${1:name} = ${2:value}\n)",
    "expect": "const (\n\tname = value\n)"
  },
  "type function declaration": {
    "actual": "type ${1:name} func($3) $4",
    "expect": "type name func() "
  },
  "type interface declaration": {
    "actual": "type ${1:name} interface {\n\t$0\n}",
    "expect": "type name interface {\n\t\n}"
  },
  "type struct declaration": {
    "actual": "type ${1:name} struct {\n\t$0\n}",
    "expect": "type name struct {\n\t\n}"
  },
  "package main and main function": {
    "actual": "package main\n\nfunc main() {\n\t$0\n}",
    "expect": "package main\n\nfunc main() {\n\t\n}"
  },
  "function declaration": {
    "actual": "func $1($2) $3 {\n\t$0\n}",
    "expect": "func ()  {\n\t\n}"
  },
  "variable declaration": {
    "actual": "var ${1:name} ${2:type}",
    "expect": "var name type"
  },
  "switch statement": {
    "actual": "switch ${1:expression} {\ncase ${2:condition}:\n\t$0\n}",
    "expect": "switch expression {\ncase condition:\n\t\n}"
  },
  "select statement": {
    "actual": "select {\ncase ${1:condition}:\n\t$0\n}",
    "expect": "select {\ncase condition:\n\t\n}"
  },
  "case clause": {
    "actual": "case ${1:condition}:$0",
    "expect": "case condition:"
  },
  "for statement": {
    "actual": "for ${1:i} := ${2:0}; $1 < ${3:count}; $1${4:++} {\n\t$0\n}",
    "expect": "for i := 0; i < count; i++ {\n\t\n}"
  },
  "for range statement": {
    "actual": "for ${1:_, }${2:v} := range ${3:v} {\n\t$0\n}",
    "expect": "for _, v := range v {\n\t\n}"
  },
  "channel declaration": {
    "actual": "chan ${1:type}",
    "expect": "chan type"
  },
  "map declaration": {
    "actual": "map[${1:type}]${2:type}",
    "expect": "map[type]type"
  },
  "empty interface": {
    "actual": "interface{}",
    "expect": "interface{}"
  },
  "if statement": {
    "actual": "if ${1:condition} {\n\t$0\n}",
    "expect": "if condition {\n\t\n}"
  },
  "else branch": {
    "actual": "else {\n\t$0\n}",
    "expect": "else {\n\t\n}"
  },
  "if else statement": {
    "actual": "if ${1:condition} {\n\t$2\n} else {\n\t$0\n}",
    "expect": "if condition {\n\t\n} else {\n\t\n}"
  },
  "if err != nil": {
    "actual": "if err != nil {\n\t${1:return ${2:nil, }${3:err}}\n}",
    "expect": "if err != nil {\n\treturn nil, err\n}"
  },
  "fmt.Println": {
    "actual": "fmt.Println(\"$1\")",
    "expect": "fmt.Println(\"\")"
  },
  "fmt.Printf": {
    "actual": "fmt.Printf(\"$1\", ${2:var})",
    "expect": "fmt.Printf(\"\", var)"
  },
  "log.Println": {
    "actual": "log.Println(\"$1\")",
    "expect": "log.Println(\"\")"
  },
  "log.Printf": {
    "actual": "log.Printf(\"$1\", ${2:var})",
    "expect": "log.Printf(\"\", var)"
  },
  "log variable content": {
    "actual": "log.Printf(\"${1:var}: %#+v\\\\n\", ${1:var})",
    "expect": "log.Printf(\"var: %#+v\\\\n\", var)"
  },
  "t.Log": {
    "actual": "t.Log(\"$1\")",
    "expect": "t.Log(\"\")"
  },
  "t.Logf": {
    "actual": "t.Logf(\"$1\", ${2:var})",
    "expect": "t.Logf(\"\", var)"
  },
  "t.Logf variable content": {
    "actual": "t.Logf(\"${1:var}: %#+v\\\\n\", ${1:var})",
    "expect": "t.Logf(\"var: %#+v\\\\n\", var)"
  },
  "make(...)": {
    "actual": "make(${1:type}, ${2:0})",
    "expect": "make(type, 0)"
  },
  "new(...)": {
    "actual": "new(${1:type})",
    "expect": "new(type)"
  },
  "panic(...)": {
    "actual": "panic(\"$0\")",
    "expect": "panic(\"\")"
  },
  "http ResponseWriter *Request": {
    "actual": "${1:w} http.ResponseWriter, ${2:r} *http.Request",
    "expect": "w http.ResponseWriter, r *http.Request"
  },
  "http.HandleFunc": {
    "actual": "${1:http}.HandleFunc(\"${2:/}\", ${3:handler})",
    "expect": "http.HandleFunc(\"/\", handler)"
  },
  "http handler declaration": {
    "actual": "func $1(${2:w} http.ResponseWriter, ${3:r} *http.Request) {\n\t$0\n}",
    "expect": "func (w http.ResponseWriter, r *http.Request) {\n\t\n}"
  },
  "http.Redirect": {
    "actual": "http.Redirect(${1:w}, ${2:r}, \"${3:/}\", ${4:http.StatusFound})",
    "expect": "http.Redirect(w, r, \"/\", http.StatusFound)"
  },
  "http.Error": {
    "actual": "http.Error(${1:w}, ${2:err}.Error(), ${3:http.StatusInternalServerError})",
    "expect": "http.Error(w, err.Error(), http.StatusInternalServerError)"
  },
  "http.ListenAndServe": {
    "actual": "http.ListenAndServe(\"${1::8080}\", ${2:nil})",
    "expect": "http.ListenAndServe(\":8080\", nil)"
  },
  "http.Serve": {
    "actual": "http.Serve(\"${1::8080}\", ${2:nil})",
    "expect": "http.Serve(\":8080\", nil)"
  },
  "goroutine anonymous function": {
    "actual": "go func($1) {\n\t$0\n}($2)",
    "expect": "go func() {\n\t\n}()"
  },
  "goroutine function": {
    "actual": "go ${1:func}($0)",
    "expect": "go func()"
  },
  "defer statement": {
    "actual": "defer ${1:func}($0)",
    "expect": "defer func()"
  },
  "test function": {
    "actual": "func Test$1(t *testing.T) {\n\t$0\n}",
    "expect": "func Test(t *testing.T) {\n\t\n}"
  },
  "test main": {
    "actual": "func TestMain(m *testing.M) {\n\t$1\n\n\tos.Exit(m.Run())\n}",
    "expect": "func TestMain(m *testing.M) {\n\t\n\n\tos.Exit(m.Run())\n}"
  },
  "benchmark function": {
    "actual": "func Benchmark$1(b *testing.B) {\n\tfor ${2:i} := 0; ${2:i} < b.N; ${2:i}++ {\n\t\t$0\n\t}\n}",
    "expect": "func Benchmark(b *testing.B) {\n\tfor i := 0; i < b.N; i++ {\n\t\t\n\t}\n}"
  },
  "example function": {
    "actual": "func Example$1() {\n\t$2\n\t//Output:\n\t$3\n}",
    "expect": "func Example() {\n\t\n\t//Output:\n\t\n}"
  },
  "table driven test": {
    "actual": "func Test$1(t *testing.T) {\n\ttestCases := []struct {\n\t\tdesc\tstring\n\t\t$2\n\t}{\n\t\t{\n\t\t\tdesc: \"$3\",\n\t\t\t$4\n\t\t},\n\t}\n\tfor _, tC := range testCases {\n\t\tt.Run(tC.desc, func(t *testing.T) {\n\t\t\t$0\n\t\t})\n\t}\n}",
    "expect": "func Test(t *testing.T) {\n\ttestCases := []struct {\n\t\tdesc\tstring\n\t\t\n\t}{\n\t\t{\n\t\t\tdesc: \"\",\n\t\t\t\n\t\t},\n\t}\n\tfor _, tC := range testCases {\n\t\tt.Run(tC.desc, func(t *testing.T) {\n\t\t\t\n\t\t})\n\t}\n}"
  },
  "init function": {
    "actual": "func init() {\n\t$1\n}",
    "expect": "func init() {\n\t\n}"
  },
  "main function": {
    "actual": "func main() {\n\t$1\n}",
    "expect": "func main() {\n\t\n}"
  },
  "method declaration": {
    "actual": "func (${1:receiver} ${2:type}) ${3:method}($4) $5 {\n\t$0\n}",
    "expect": "func (receiver type) method()  {\n\t\n}"
  },
  "hello world web app": {
    "actual": "package main\n\nimport (\n\t\"fmt\"\n\t\"net/http\"\n\t\"time\"\n)\n\nfunc greet(w http.ResponseWriter, r *http.Request) {\n\tfmt.Fprintf(w, \"Hello World! %s\", time.Now())\n}\n\nfunc main() {\n\thttp.HandleFunc(\"/\", greet)\n\thttp.ListenAndServe(\":8080\", nil)\n}",
    "expect": "package main\n\nimport (\n\t\"fmt\"\n\t\"net/http\"\n\t\"time\"\n)\n\nfunc greet(w http.ResponseWriter, r *http.Request) {\n\tfmt.Fprintf(w, \"Hello World! %s\", time.Now())\n}\n\nfunc main() {\n\thttp.HandleFunc(\"/\", greet)\n\thttp.ListenAndServe(\":8080\", nil)\n}"
  },
  "sort implementation": {
    "actual": "type ${1:SortBy} []${2:Type}\n\nfunc (a $1) Len() int           { return len(a) }\nfunc (a $1) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }\nfunc (a $1) Less(i, j int) bool { ${3:return a[i] < a[j]} }",
    "expect": "type SortBy []Type\n\nfunc (a SortBy) Len() int           { return len(a) }\nfunc (a SortBy) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }\nfunc (a SortBy) Less(i, j int) bool { return a[i] < a[j] }"
  }
}


@pytest.mark.parametrize('name', [name for name in test_case])
def test_replace_textmate_syntax(name):
    actual = test_case[name]['actual']
    expect = test_case[name]['expect']
    assert replace_textmate_syntax(actual) == expect
