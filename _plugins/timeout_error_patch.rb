require "timeout"

# Ruby 3 removed the top-level TimeoutError constant that legacy plugins expect.
# Define the alias within the namespaces Jekyll::Gist searches during constant lookup,
# so the rescue clause in jekyll-gist continues to work.
TimeoutError = Timeout::Error unless defined?(TimeoutError)

module Jekyll
  module Gist
    TimeoutError = Timeout::Error unless const_defined?(:TimeoutError)
  end
end

