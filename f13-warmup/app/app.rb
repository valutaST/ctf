require 'webrick'
$SOURCE_CODE = File.read(__FILE__)


class SimpleServlet < WEBrick::HTTPServlet::AbstractServlet
  def do_GET(request, response)
    response.status = 200
    response.content_type = 'text/html'    
    
    if request.query.key?('message')
      @message = request.query['message']
      @message = ERB.new('A message has been sent to: ' + @message).result(binding)
    else
      @message = ""
    end

    response.body = ERB.new(File.read('views/index.html')).result(binding)
  end
end

server = WEBrick::HTTPServer.new(Port: 30002, BindAddress: '0.0.0.0')
server.mount('/assets', WEBrick::HTTPServlet::FileHandler, './assets')
server.mount('/', SimpleServlet)

trap('INT') { server.shutdown }

server.start