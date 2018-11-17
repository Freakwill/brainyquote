
command: "python3 brainyquote/quote.py"

render: (output) -> "<quote>#{output}</quote>"


style: """
  top: 10px
  right: 10px
  background: rgba(#fff, 0.6) url('brainyquote/flower.png') no-repeat 50% 20px
  background-size: 200px 84px
  border-radius: 0px
  border: 0px solid #fff
  box-sizing: border-box
  font-family: Helvetica Neue
  line-height: 1.5
  padding: 120px 20px 20px
  width: 340px
  text-align: justify

  quote
    color: blue
    font-weight: 500
"""

update: (output, _) -> "#{output}"

refreshFrequency: 1000 * 3600 * 24 * 2
